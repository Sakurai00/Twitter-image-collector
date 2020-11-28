import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get("TW_KEY")
CONSUMER_SECRET = os.environ.get("TW_KEY_SEC")
ACCESS_TOKEN_KEY = os.environ.get("TW_ACC_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TW_ACC_TOKEN_SEC")


NO_INPUT = True
SEARCH_NUM = 1000
MIN_FAV = 50
TARGET_WORD = "#シオンの書物"


"""
#プロテインザスバル
#シオンの書物
#百鬼絵巻
#ヌォンタート
"""

"""
API 15 min / 180(user) 450(app)
3200 tweets ?
"""