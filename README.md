> pip install -r requirements.txt

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

### 2. DAO and DTO(VO)

- DAO(Data Access Object): CRUD 할 때 사용
  - Create: INSERT
  - Read: SELECT
  - Update: UPDATE
  - Delete: DELETE
- DTO(Data Transfer Object): 데이터를 전달할 때 사용

### 3. 유효성(Validation) 체크

- 유효성체크는 사용자의 값이 올바른 값인지 체크
  - 예: 이메일(이메일 형식인지)
- 역사
  1.  유효성체크: 서버 -> 과부하
  2.  클라이언트(웹브라우저) -> JS (사용중)
  3.  서버 추가 -> 더블 체크(pydantic)

### 4. 웹 동작 과정 PROCESS

- 정의: Client(=Web browser) , Server(회사)
- 동작 : Client -> request -> Server -> response
- 동작(심화) : View단(Client) -> Controller단(main,router) -> Service단 -> Model단(DB)

  - View단: 사용자에게 보여지는 화면
  - Controller단: 사용자가 요청한 URL과 데이터(유효성체크)를 전달받고 일을 분배하는 곳
  - Service단: 실제 기능 구현
  - Model단: DB관련 된 기능 구현(DAO)

  1.  Client에서 form 또는 ajax 등을사용해서 request(+data) # fnc.js의 $.ajax

  - URL: http://127.0.0.1:8000/kakao/
  - method: POST
  - data: json

  2. Server의 main.py에서 요청을 받기 -> 해당 라우터로 전달
  3. Server의 해당 Router(kakao)에서 request와 data를 받음

  - pydantic을 활용한 data validation check(유효성 검증) -> data

  4. Server의 Service단으로 request와 data를 전달

### 5. Web과 DB

- 2가지 방법(SQL 매핑, ORM)
- SQL 매핑: web서버 -> DB 커넥션 -> SQL 작성 -> DB에서 SQL 실행 -> Web서버 결과 받기
- ORM: DB의 테이블 객체화 시켜서 사용하는 방법(최신), SQL 사용 안함, 확장성 및 유지보수 등 용이

* Web서버 -> DB 커넥션 -> ORM(객체화) -> ORM 사용 -> Web서버 결과 받기

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

### LLM 모델 신기술: RAG(검색증강생성)

기존 LLM 모델의 단점

1. 최신 내용 반영 X -> 최신 내용 반영하도록 재학습(시간, 자원) / 비효율적

RAG 방법

- 기존에 추가해야하는 내용 -> 임베딩 -> Vector DB에 저장

1. 사용자 질문
   - 사용자 질문과 Vector DB에 있는 값들간의 유사도를 계산해서 비슷한 내용을 추출
   - 추출한 내용과 사용자 질문을 함께 LLM모델에 전달
   - LLM 모델이 Vector DB(질문과 유사한 값)에 있는 값을 활용해서 답변을 생성
