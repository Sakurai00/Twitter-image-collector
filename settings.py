import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get("TW_KEY")
CONSUMER_SECRET = os.environ.get("TW_KEY_SEC")
ACCESS_TOKEN_KEY = os.environ.get("TW_ACC_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TW_ACC_TOKEN_SEC")



SEARCH_NUM = 1000
MIN_FAV = 50

NO_INPUT = True
TARGET_WORD = "#シオンの書物"

MULTI_SEARCH = True
MULTI_TARGET_WORD = [
    "#プロテインザスバル",
    "#シオンの書物",
    "#百鬼絵巻",
    "#みおーん絵"
    ]


"""
#プロテインザスバル
#シオンの書物
#百鬼絵巻
#ヌォンタート
#みおーん絵
"""

"""
API 15 min / 180(user) 450(app)
3200 tweets ?
"""