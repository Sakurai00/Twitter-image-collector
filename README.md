# Twitter-image-collector

ツイートの検索結果に含まれる画像を./images/TARGET_WORD/に保存する

## Requirement
- Windows
- python 3.9.6
- tweepy 4.0.1
- python-dotenv


## Installation
```bash
poetry install
```

.envにtokenを書く
```
TW_KEY=***
TW_KEY_SEC=***
TW_ACC_TOKEN=***
TW_ACC_TOKEN_SEC=***
```

## Usage
```bash
poetry run python -m twcollector

poetry run python -m twcollector -s "#Hololive"
```
