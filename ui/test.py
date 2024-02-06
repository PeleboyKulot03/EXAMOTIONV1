import json
import requests

headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjk2YzVlNDItMWJmYi00MjdjLWE3YmYtMTk1NTFiMWE3YjMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.T8vEDl5ARjIWecUThzD3FI1zTOzq4xBbsMkEXZnWW9o"}

url = "https://api.edenai.run/v2/text/emotion_detection"
payload = {
    "providers": "nlpcloud,vernai",
    "text": "I am angry!",
    "fallback_providers": ""
}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
print(result["nlpcloud"]["items"])
