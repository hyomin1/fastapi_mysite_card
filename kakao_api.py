# 카카오 API를 사용해서 나에게 톡 보내기
# 1. Kakao Developer 설정
# 2. 인증 코드 요청 -> 카카오 서버 -> 인증 코드 전달(인증 코드 1회성 -> 토큰 1회 발급받음과 동시에 효력X) 
# 3. 인증 코드를 사용해서 토큰 발급
# 4. 토큰을 사용해서 나에게 메세지 보내기
import requests


# 1. 카카오 OAuth URL과 Redirect Key를 사용해서 인증 코드 요청
# - 웹 브라우저 URL:https://kauth.kakao.com/oauth/authorize?client_id=1872018566f45c5add75690ea13d2d09&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message
# - 위의 코드를 웹 브라우저 URL에 입력하고 엔터누르면 새로운 URL로 변경 code=[???]
# - [???] -> 카카오로부터 전달받은 인증코드

# 2.인증코드를 사용해서 토큰 발급 받기
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "1872018566f45c5add75690ea13d2d09",    # RESTAPI KEY
    "redirect_uri" :"http://127.0.0.1:8000",  
    "code":"R-JtQQykZwz4vzAJ1ecwvrhxDoMf-8azeCfo8fqF2X1KoqOV5dBw7h_TKLcKKcjaAAABjsDrS3rHP8VuE1ZNOQ",
}

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)
