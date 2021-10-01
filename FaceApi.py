import requests
from PIL import Image
import json

with open("secret.json") as f:
    secret_json=json.load(f)
SUBSCRIPTION_KEY=secret_json["SUBSCRIPTION_KEY"]
print(SUBSCRIPTION_KEY)