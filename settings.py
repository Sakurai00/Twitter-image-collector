import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get("TW_KEY")
CONSUMER_SECRET = os.environ.get("TW_KEY_SEC")
ACCESS_TOKEN_KEY = os.environ.get("TW_ACC_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TW_ACC_TOKEN_SEC")


SEARCH_NUM = 500
TARGET_WORD = "#ヌォンタート"
"""
#シオンの書物
#百鬼絵巻
#ヌォンタート
"""
