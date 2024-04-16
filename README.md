# fastapi_mysite_card

### 라이브러리 설명

1. fastapi : 웹 프레임워크 + API
2. uvicorn: WAS(웹 어플리케이션 서버)
3. jinja2: 템플릿 엔진(HTML, CSS, JS)

### Web 프로그래밍 기초 설명

#### 1.URL

    - http://127.0.0.1:8080 = http://localhost:8000
    - 127.0.0.1과 localhost는 루프백 주소(현재 디바이스의 IP를 의미)
    - http -> 프로토콜
    - 8000 -> Port 번호
    - http 프로토콜에서 제공하는 함수(get, post, put, delete)
    - http://127.0.0.1:8000/member?id=abc1234&name=cherry -> 쿼리스트링(get 방식)
    - 숨겨야하는 정보들(post 방식)

### 카카오 나에게 톡 보내기

- 인증코드 URL(Base) : https://kauth.kakao.com/oauth/authorize?client_id={REST API 키}&redirect_uri={Redirect URI}&response_type=code&scope=talk_message
- 인증 코드 URL(Me): https://kauth.kakao.com/oauth/authorize?client_id=1872018566f45c5add75690ea13d2d09&redirect_uri=http://127.0.0.1:8000&response_type=code&scope=talk_message

#### 1. 카카오 API 용어

- 인증코드 : 1회성, 토큰(Access, Refresh)
  발급받기 위해 사용!
- Access 토큰: 카카오 API 서비스를 이용할 때 사용
- Refresh 토큰: Access 토큰을 재발급 받기 위해 사용
- 생명주기: 인증코드(1회), Access(6시간), Refresh(2달)
- \*Refresh Token은 발급받고 1달 후부터 재발급 가능
- Access와 Refresh 재발급 받는 코드는 동일
- ㄴ 재발급 코드 : Refresh 발급받은지 1달 미만, Access 토큰만 재발급 해서 리턴
- ㄴ 재발급 코드 : Refresh 발급받은지 1달 이상, Refresh 토큰 재발급 해서 리턴

#### 2. 카카오 API 사용 방법

1. Kakao Developer 사이트에서 "권한 허용 및 동의"
2. 웹브라우저 URL을 통해서 인증 코드 발급
3. 인증코드 사용해서 토큰 (Access, Refresh)발급
4. Access 사용해서 서비스 이용!
5. - 1달에 한번씩 Refresh 토큰 재발급 스케줄링
