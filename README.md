# Face_Detect_App

- [参考](https://www.youtube.com/watch?v=zpBjbK6jic0&list=WL&index=12&t=232s)

## 準備

- `pip install -r requirements.txt`

### pandas のインストール

- `pip install pandas`

### M1 Mac などで pandas のインストールに失敗した場合

- `git clone https://github.com/pandas-dev/pandas.git`
- `cd pandas`
- `python3 setup.py install --record files.txt`

## 実行

- [Microsoft](https://azure.microsoft.com/ja-jp/services/cognitive-services/face/#overview)アカウントを作成・ログインして、Face API を始める。
- secret.json ファイルを作成して SUBSCRIPTION_KEY と ENDPOINT を JSON 形式で記載する。
- `streamlit run main.py`を実行
  > Mac 以外の環境の場合、FaceApi.py の font_path を各自の環境に合わせて調整してから実行してください。
