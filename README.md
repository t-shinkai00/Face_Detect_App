# Face_Detect_App

- アップロードした画像に対して顔検出を行う。
- 顔検出されれば顔のある領域が白色の長方形で囲まれる。
- また長方形の上に性別、推定年齢が示される。
- [実際に試す](https://share.streamlit.io/t-shinkai00/face_detect_app/main/main.py)
  ![](images/scrnli_10_9_2021_2-41-57%20AM.png)

## 実行準備

### 自分の環境にモジュール類をインストールする場合

- `pip install -r requirements.txt`

### M1 チップ搭載 Mac を使用していて Pandas のインストールに失敗した場合

- `git clone https://github.com/pandas-dev/pandas.git`
- `cd pandas`
- `python setup.py install --record files.txt`

## 実行

- [Microsoft](https://azure.microsoft.com/ja-jp/services/cognitive-services/face/#overview)アカウントを作成・ログインして、Face API を始める。
- secret.json ファイルを作成して SUBSCRIPTION_KEY と ENDPOINT を JSON 形式で記載する。
- `streamlit run main.py`を実行。
