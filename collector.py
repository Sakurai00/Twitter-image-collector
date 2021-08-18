import os
import time
import urllib

import tweepy

import twapi
import settings as st


api = twapi.generate_api()

def set_search_str():
    """ 入力orコンフィグファイルから検索ワードを取得してセットする

    Returns:
        String: 検索ワード
    """

    buf = input("use default word -> 0 :")

    if buf == str(0):
        return st.TARGET_WORD
    else:
        return buf


def make_dir(search_str):
    """ ディレクトリを作成する

    Args:
        search_str (String): 検索ワード
    """

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(".\\image")
    if not os.path.exists(search_str):
        os.mkdir(search_str)
    os.chdir(search_str)
    return


def search(search_str):
    """ 検索ワードで検索して画像をダウンロードする

    Args:
        search_str (String): 検索ワード
    """

    sum = 1
    pic = 0
    if str(st.MIN_FAV) == 0:
        q = search_str + " filter:images exclude:retweets"
    else:
        q = search_str + " filter:images exclude:retweets min_faves:" + str(st.MIN_FAV)
    print(q)
    tweets = tweepy.Cursor(api.search, q = q).items(st.SEARCH_NUM)

    for tweet in tweets:
        sum += 1
        if "media" in tweet.entities:
            pic += 1
            for tweet_media in tweet.entities["media"]:
                url = tweet_media["media_url_https"]
                print(pic, "/", sum, " ",end = "")
                download(url)
    return


def download(url):
    """ Twitterのmediaリンクから画像をダウンロードする

    Args:
        url (String): Twitter media link
    """

    file_name = url.split('/')[-1]
    url += ":orig"
    if os.path.isfile(file_name):
        print("pass")
    else:
        print(url)
        try:
            urllib.request.urlretrieve(url, file_name)
        except Exception as e:
            print("Error")
    return


def main():
    t1 = time.time()

    if st.MULTI_SEARCH == True:
        for search_str in st.MULTI_TARGET_WORD:
            make_dir(search_str)
            search(search_str)
    else:
        if st.NO_INPUT == True:
            search_str = st.TARGET_WORD
        else:
            search_str = set_search_str()
        make_dir(search_str)
        search(search_str)

    t2 = time.time()
    print(t2 - t1, "sec")
    return


if __name__ == '__main__':
    main()
