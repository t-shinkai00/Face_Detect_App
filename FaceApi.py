import requests
from PIL import Image
import json

with open("secret.json") as f:
    secret_json=json.load(f)
SUBSCRIPTION_KEY=secret_json["SUBSCRIPTION_KEY"]
ENDPOINT=secret_json["ENDPOINT"]
# print(SUBSCRIPTION_KEY)
assert SUBSCRIPTION_KEY
face_api_url=ENDPOINT+"face/v1.0/detect"
# print(face_api_url)