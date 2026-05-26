# CLOVA OCR API — Text Extraction Guide

Extract text from image files using the Naver CLOVA OCR API.  
This guide walks you through authentication, request format, and response handling.

---

## Overview

The CLOVA OCR API analyzes image files and returns all recognized text with position data. It supports printed and handwritten Korean, English, and Japanese.

**Base URL**

    https://clovaocr-api-kr.ncloud.com/external/v1/{domainUID}/{domainKey}/general

---

## Authentication

All requests require a secret key in the request header.

| Header | Type | Description |
|---|---|---|
| X-OCR-SECRET | string | Secret key issued from CLOVA OCR Console[https://console.ncloud.com/ocr/domain] |

---

## Request

**Method:** POST  
**Content-Type:** application/json

### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| version | string | Yes | API version. Use `V2` |
| requestId | string | Yes | Unique ID for the request |
| timestamp | integer | Yes | Current timestamp in milliseconds |
| images | array | Yes | List of image objects to process |

### Image Object

| Field | Type | Required | Description |
|---|---|---|---|
| format | string | Yes | Image format. `jpg`, `png`, `pdf`, `tiff` |
| name | string | Yes | Identifier for the image |
| data | string | Yes | Base64-encoded image data |

### Example Request

    import requests
    import base64
    import os
    from dotenv import load_dotenv

    load_dotenv()
    API_URL = os.getenv("API_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")

    with open("invoice.jpg", "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "version": "V2",
        "requestId": "sample-001",
        "timestamp": 0,
        "images": [
            {
                "format": "jpg",
                "name": "invoice",
                "data": image_data
            }
        ]
    }

    headers = {
        "X-OCR-SECRET": SECRET_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())

---

## Response

### Response Fields

| Field | Type | Description |
|---|---|---|
| version | string | API version |
| requestId | string | Request ID passed in the request |
| timestamp | integer | Time the request was processed |
| images | array | List of recognition result objects |

### Image Result Object

| Field | Type | Description |
|---|---|---|
| inferResult | string | Recognition status. `SUCCESS` or `ERROR` |
| fields | array | List of recognized text blocks |

### Field Object

| Field | Type | Description |
|---|---|---|
| inferText | string | Recognized text content |
| inferConfidence | float | Confidence score (0 to 1) |
| boundingPoly | object | Coordinates of the text block in the image |

### Example Response

    {
        "version": "V2",
        "requestId": "sample-001",
        "timestamp": 1779771106090,
        "images": [
            {
                "inferResult": "SUCCESS",
                "fields": [
                    {
                        "inferText": "Invoice",
                        "inferConfidence": 0.9977,
                        "boundingPoly": {
                            "vertices": [
                                {"x": 401.0, "y": 230.0},
                                {"x": 487.0, "y": 230.0},
                                {"x": 487.0, "y": 250.0},
                                {"x": 401.0, "y": 250.0}
                            ]
                        }
                    }
                ]
            }
        ]
    }

---

## Error Codes

| Status Code | Description |
|---|---|
| 200 | Success |
| 401 | Invalid or missing Secret Key |
| 404 | Domain not found |
| 500 | Internal server error |

---

## Notes

- Supported image formats: `jpg`, `png`, `pdf`, `tiff`
- Maximum file size: 50MB
- Minimum resolution: 150dpi (A4 standard)
- `.env` file is required for API credentials. Never hardcode keys in source code.