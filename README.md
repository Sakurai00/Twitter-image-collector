# Twitter-image-collector

ツイートの詮索結果に含まれる画像ファイルを.\image\TARGET_WORD\に保存する

# settings
- MULTI_SEARCH = True  
NO_INPUTに関わらずMULTI_SEARCHを実行する。

- MULTI_SEARCH = False, NO_INPUT = True  
TARGET_WORDを入力させず、settings.pyのTARGET_WORDで検索を実行する。


# token
.envにtokenを書く。
```
TW_KEY=***
TW_KEY_SEC=***
TW_ACC_TOKEN=***
TW_ACC_TOKEN_SEC=***
```
