import requests
import base64
from dotenv import load_dotenv
import os

# .env 파일에서 키 불러오기
load_dotenv()
API_URL = os.getenv("API_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# 테스트할 이미지 파일 경로
IMAGE_PATH = "test.jpg"

# 이미지를 base64로 변환
with open(IMAGE_PATH, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# API 요청
payload = {
    "images": [
        {
            "format": "jpg",
            "name": "test",
            "data": image_data
        }
    ],
    "requestId": "test-001",
    "version": "V2",
    "timestamp": 0
}

headers = {
    "X-OCR-SECRET": SECRET_KEY,
    "Content-Type": "application/json"
}

response = requests.post(API_URL, headers=headers, json=payload)