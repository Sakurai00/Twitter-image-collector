import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get("TW_KEY")
CONSUMER_SECRET = os.environ.get("TW_KEY_SEC")
ACCESS_TOKEN_KEY = os.environ.get("TW_ACC_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TW_ACC_TOKEN_SEC")



SEARCH_NUM = 1000
MIN_FAV = 800

NO_INPUT = True
TARGET_WORD = "#まのあろ絵"

MULTI_SEARCH = True
MULTI_TARGET_WORD = [
    "#みおーん絵",
    "#プロテインザスバル",
    "#シオンの書物",
    "#百鬼絵巻",
    "#あくあーと",
    "#はあとart",
    "#絵かゆ",
    "#絵クロマンサー",
    "#ししらーと",
    "#LamyArt"
    ]


"""
#あくあーと
#プロテインザスバル
#シオンの書物
#百鬼絵巻
#みおーん絵
#ヌォンタート
#はあとart
#絵かゆ
#絵クロマンサー
#LamyArt
#ししらーと
"""
