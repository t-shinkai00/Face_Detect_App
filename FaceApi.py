import requests
from PIL import Image
from PIL import ImageDraw
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

headers={
  "Content-Type":"application/octet-stream",
  "Ocp-Apim-Subscription-Key":subscription_key
  }
params={
  "returnFaceId":"true",
  "returnFaceAttributes":"age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure, noise",
}
res=requests.post(face_api_url, params=params, headers=headers, data=binary_img)
# print(res)


results=res.json()
# print(results)
for result in results:
  rect=result["faceRectangle"]
  # print(rect)
  age=result["faceAttributes"]["age"]
  gender=result["faceAttributes"]["gender"]
  # print(age,gender)

  draw=ImageDraw.Draw(img)
  # draw.line([(0,50),(200,50),(0,150),(200,150)],fill="red",width=5)
  # img.show()

  draw.rectangle([(rect["left"], rect["top"]), (rect["left"]+rect["width"], rect["top"]+rect["height"])])
img.show()