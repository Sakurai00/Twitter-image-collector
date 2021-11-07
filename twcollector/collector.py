import argparse
import os
import pathlib
import time
import urllib.request

import tweepy
from twapi.twapi import generate_api

import twcollector.settings as st

api = generate_api()


def make_dir(search_str):
    """ディレクトリを作成する

    Args:
        search_str (String): 検索ワード
    """

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    path = base_dir / "images" / search_str
    if not path.exists():
        path.mkdir(parents=True)
    os.chdir(path)
    return


def search(search_str, min_fav):
    """検索ワードで検索して画像をダウンロードする

    Args:
        search_str (String): 検索ワード
        min_fav (String): 最低fav数
    """

    sum = 1
    pic = 0
    if min_fav == 0:
        q = search_str + " filter:images exclude:retweets"
    else:
        q = search_str + " filter:images exclude:retweets min_faves:" + min_fav
    print(q)
    tweets = tweepy.Cursor(api.search_tweets, q=q).items(st.SEARCH_NUM)

    for tweet in tweets:
        sum += 1
        if "media" in tweet.entities:
            pic += 1
            for tweet_media in tweet.entities["media"]:
                url = tweet_media["media_url_https"]
                print(pic, "/", sum, " ", end="")
                download(url)
    return


def download(url):
    """Twitterのmediaリンクから画像をダウンロードする

    Args:
        url (String): Twitter media link
    """

    file_name = url.split("/")[-1]
    url += ":orig"
    if os.path.isfile(file_name):
        print("pass")
    else:
        print(url)
        try:
            res = urllib.request.urlopen(url).read()
            with open(file_name, "wb") as f:
                f.write(res)
        except urllib.error.HTTPError as e:
            print(e.reason)
    return


def main():
    parser = argparse.ArgumentParser(description="Twitter image collector")
    parser.add_argument("-s", "--search", help="search word")
    parser.add_argument("-f", "--fav", help="min fav")
    arg = parser.parse_args()

    t1 = time.time()

    min_fav = st.MIN_FAV
    if arg.fav is not None:
        min_fav = arg.fav
    min_fav = str(min_fav)

    if arg.search is None:
        for search_str in st.TARGET_WORDS:
            make_dir(search_str)
            search(search_str, min_fav)
    elif arg.search is not None:
        make_dir(arg.search)
        search(arg.search, min_fav)

    t2 = time.time()
    print(t2 - t1, "sec")
    return
