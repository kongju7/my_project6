## [여섯 번째 프로젝트]: 음성 인식 딥러닝 챗봇 - GUI 및 웹 인터페이스 구현

- 작성: 2023년 2월 14일
- 웹 애플리케이션 파일: pytorch_chatbot 폴더

### 프로젝트 개요


1. 주제 및 데이터 소개: **음성 인식 딥러닝 챗봇** 

    - 판별 AI: PyTorch 기반 - 자연어 처리 딥러닝 모델 생성 및 학습
        - 데이터: 시나리오 기반 json 형식으로 직접 작성
            - 태그(tag), 패턴(pattern), 응답(response) 항목 포함 →  **상황별 확장 가능**
    - 음성 인식 기능: Python, JavaScript 함수 활용
    - 2종의 인터페이스 구현: Python GUI, Flask 기반 웹 인터페이스

2. 자연어 처리 딥러닝 모델 생성: PyTorch 기반 - 화자의 ‘의도’ 판별 →  응답 반환  

    - 한글 토큰화, 한글 표제어 추출
    	- [한국어 용언 분석기(Korean Lemmatizer)](https://github.com/lovit/korean_lemmatizer) 사용
	- 딥러닝 모델 생성 및 학습  
    	- PyTorch 라이브러리 함수 활용: 하이퍼 파라미터 설정  
    	- 모델 학습 진행 및 모델 저장  
    	    - Epoch 1000 - final loss: 0.0001   
3. 음성 인식 기능 

    - Python GUI : Python - SpeechRecognition 라이브러리 활용
    - 웹 인터페이스:  JavaScript - webkitSpeechRecognition 라이브러리 활용 → 음성 저장 및 전송을 html 상에서 처리하여 결과를 전송하도록 구현  
4. 2종의 인터페이스 구현  

    - Python GUI 구현: Tkinter 라이브러리 활용
    
<img src = "https://raw.githubusercontent.com/kongju7/my_project6/main/img/cp2_2nd.png" width="50%" height="50%">

<img src = "https://raw.githubusercontent.com/kongju7/my_project6/main/img/chatbot_gui_run.png" width="50%" height="50%">


   - 웹 인터페이스 구현: Flask 기반 - HTML, JavaScript, CSS 등 활용
    
<img src = "https://raw.githubusercontent.com/kongju7/my_project6/main/img/cp2_flask.png" width="50%" height="50%">
    
<img src = "https://raw.githubusercontent.com/kongju7/my_project6/main/img/chatbot_web.png" width="65%" height="65%">

5. 평가 및 향후 계획 

	- [기존 챗봇 프로젝트](https://github.com/kongju7/my_project4)에서 진일보
    	- PyTorch 기반 자연어 처리 딥러닝 모델 직접 구현
    	- 음성 인식 기능 추가
    	- 2종의 서로 다른 인터페이스 구현
	- 향후 계획
    	- 대용량 데이터 확보를 통한 모델 성능 재평가
    	- 개체명 인식(NER) 기법을 활용한 서비스 정교화
  	
  	
  
### [참고] 챗봇 실행 방법
  
- 딥러닝 모델 학습 실행 및 저장    
  
```Shell 
make train 
```
  
- 챗봇 - Python GUI 실행   
  
```Shell 
make run
```
    
- 챗봇 - Flask 기반의 웹 인터페이스 실행 
  
```Shell 
make flask 
```
