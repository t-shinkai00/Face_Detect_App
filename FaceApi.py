import requests
from PIL import Image
import json

with open("secret.json") as f:
  secret_json=json.load(f)
subscription_key=secret_json["SUBSCRIPTION_KEY"]
endpoint=secret_json["ENDPOINT"]

# print(subscription_key)
assert subscription_key
face_api_url=endpoint+"face/v1.0/detect"
# print(face_api_url)

img=Image.open("images/Jack-U.jpg")
# img.show()

with open("images/Jack-U.jpg","rb") as f:
  binary_img=f.read()
# print(binary_img)