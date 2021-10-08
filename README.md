# Face_Detect_App

- [デプロイ先](https://share.streamlit.io/t-shinkai00/face_detect_app/main/main.py)

## 実行準備

### 自分の環境にモジュール類をインストールする場合

- `pip install -r requirements.txt`

### venv 環境を用いる場合

- `source .face-detect-app/bin/activate`

## 実行

- [Microsoft](https://azure.microsoft.com/ja-jp/services/cognitive-services/face/#overview)アカウントを作成・ログインして、Face API を始める。
- secret.json ファイルを作成して SUBSCRIPTION_KEY と ENDPOINT を JSON 形式で記載する。
- `streamlit run main.py`を実行
  > Mac 以外の環境の場合、FaceApi.py の font_path を各自の環境に合わせて調整してから実行してください。
