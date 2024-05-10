from dotenv import load_dotenv, find_dotenv
from backend.schemas.message import MessageDTO
import os
import requests
import json

_ = load_dotenv(find_dotenv())
url = "https://kauth.kakao.com/oauth/token"

client_id = os.getenv("KAKAO_REST_API_KEY")
redirect_uri = os.getenv("KAKAO_REDIRECT_URI")
auth_code="sb6VmRKLsJ8U4mtKZDMLWcXLdU1YBRYodVgJsFYEZfLKuZ-y5qwJjjYWgpAKPXTZAAABj1Dl9cIh5oEAb4_jFQ"
class KakaoService:

    # 카카오 토큰 발급받기(+ 인증코드)
    def refresh_access_token(self):
        # kakao_code.json 파일에서 token 불러오기
        with open("./kakao_code.json","r") as fp:
            tokens = json.load(fp)
            
        # refresh_token 추출
        refresh_token = tokens["refresh_token"]
        
        # refresh_token을 사용해서 access_token 재발급
        data = {
            "grant_type":"refresh_token",
            "client_id": client_id,
            "refresh_token": refresh_token
        }
        
        response = requests.post(url, data=data)
        new_tokens = response.json()

        # Refresh_token으로 access_token 재발급 받는 경우 2가지
        # - refresh_token(2달, 1달 이후 부터 재발급 가능)
        # 1. refresh_token 발급받고 1달 이내
        #    response(new access_token만 발급)
        # 2. refresh_token 발급받고 1달 이후
        #    response(new access_token, new refresh_token 발급)

        # tokens -> kakao_code.json(예전 토큰들...)
        if new_tokens.get("refresh_token"): # refresh_token도 재발급 된 경우
            tokens["refresh_token"] = new_tokens.get("refresh_token") # refresh_token 최신화
        
        tokens["access_token"] = new_tokens.get("access_token") # access_token 최신화

        # 재발급한 토큰 kakao_code.json에 저장
        with open("./kakao_code.json","w") as fp:
            json.dump(tokens, fp)
        return tokens

    # Access Token 재발급(+ Refresh Token)
    def get_first_token(self):
        
        data = {
            "grant_type" : "authorization_code",
            "client_id" : client_id,    # RESTAPI KEY
            "redirect_uri" :redirect_uri,  
            "code":auth_code,
        }

        response = requests.post(url,data=data)
        tokens = response.json() # 최초 토큰 발급 받기
        

        # 발급 받은 토큰 kakao_code.json에 저장
        with open("./kakao_code.json", "w") as fp:
            json.dump(tokens, fp)
        return tokens
        

    # 나에게 카카오톡 보내기
    def send_message(self, msg:MessageDTO):
        
        # 1. 토큰 유무 체크
        # ./kakao_code.json -> Access_token, Refresh_token 저장
        if os.path.isfile("./kakao_code.json"):
            # 동작: kakao_code.json 파일이 존재한다면
            #       refresh_token을 사용해서 Access_token 재발급
            #        Access_token은(4시간만 사용 가능)
            tokens = self.refresh_access_token()
        else:
            # 동작: kakao_code.json 파일이 없다면
            #       토큰을 발급받은적이 없기 때문에
            #       최초로 Access_token과 Refresh_token을 발급받고
            #       kakao.code_json에 저장
            
            tokens = self.get_first_token()
            
        # 2. Access Token을 사용해서 나에게 카카오톡 보내기
        # kakao_code.json 유무와 상관없이 토큰(Access, Refresh)
        msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers = {
        "Authorization" : "Bearer " + tokens["access_token"]
        }
        msg_data = {
            "template_object": json.dumps({
            "object_type": "text",
            "text":f"이름: {msg.name} \n메일: {msg.email} \n메세지: {msg.message}",
            "link":{"mobile_web_url":"http://127.0.0.1:8000"}
            })
}
        response = requests.post(msg_url, headers=headers, data=msg_data)

        if response.json().get("result_code") == 0:
            print("메세지를 성공적으로 보냈습니다.")
        else:
            print("메세지를 보내는데 실패했습니다. Error: " + str(response.json()))


        

        # 3. DB에 저장

        # +. 스케줄러 등록(Refresh Token 재발급)
        #  - Refresh Token은 유효기간 2달
        #  - 그리고 발급받은 날짜로부터 1달 후 재발급 가능
        #  - 스케줄러 -> 1달에 한번씩 Refresh Token을 재발급