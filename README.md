# CLOVA OCR API Practice

이미지에서 텍스트를 자동으로 추출하는 Python 스크립트입니다.
Naver CLOVA OCR API를 활용하며, Lomin Textscope API와 동일한 구조로 작동합니다.

---

## 개요

이 프로젝트는 OCR(광학 문자 인식) API를 호출해 이미지 파일에서 텍스트를 추출하고 출력하는 예제입니다.

활용 시나리오 예시
- 스캔된 문서에서 텍스트 데이터 추출
- 인보이스, 영수증 이미지에서 주요 정보 자동 수집
- 추출된 텍스트를 Google Sheets 등 외부 서비스와 연동

---

## 사용 기술

- Python 3
- Naver CLOVA OCR API
- python-dotenv (환경변수 관리)
- requests (HTTP 통신)

---

## 시작하기

### 1. 패키지 설치

    pip3 install requests python-dotenv

### 2. 환경변수 설정

.env 파일을 생성하고 아래 내용을 입력합니다.

    API_URL=발급받은_APIGW_Invoke_URL/general
    SECRET_KEY=발급받은_Secret_Key

### 3. 이미지 준비

텍스트가 포함된 이미지를 test.jpg 이름으로 프로젝트 폴더에 저장합니다.

### 4. 실행

    python3 ocr_test.py

---

## 출력 예시

    Problem
    Hypothetical Situation
    1st Reason
    2nd Reason

---

## 주의사항

- .env 파일은 .gitignore에 포함되어 있어 GitHub에 업로드되지 않습니다.
- API 키를 코드에 직접 입력하지 마세요.