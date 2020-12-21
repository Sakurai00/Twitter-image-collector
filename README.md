# Twitter-image-collector

ツイートの検索結果に含まれる画像ファイルを.\image\TARGET_WORD\に保存する

## Requirement

- python 3.8.5
- tweepy 3.9.0


## Installation
```bash
pip install tweepy
```

.envにtokenを書く
```
TW_KEY=***
TW_KEY_SEC=***
TW_ACC_TOKEN=***
TW_ACC_TOKEN_SEC=***
```

## Settings
- MULTI_SEARCH = True  
NO_INPUTに関わらずMULTI_SEARCHを実行する。

- NO_INPUT = True  
TARGET_WORDを入力させず、settings.pyのTARGET_WORDで検索を実行する。
