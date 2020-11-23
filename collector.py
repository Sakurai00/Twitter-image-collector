import tweepy, os, urllib, time
import settings as st

auth = tweepy.OAuthHandler(st.CONSUMER_KEY, st.CONSUMER_SECRET)
auth.set_access_token(st.ACCESS_TOKEN_KEY, st.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def set_search_str():
    buf = input("use default word -> 1 :")
    if buf == 1:
        return st.TARGET_WORD
    else:
        return buf

def search(search_str):
    sum = 1
    pic = 0
    q = search_str + "exclude:retweets"
    tweets = tweepy.Cursor(api.search, q = q).items(st.SEARCH_NUM)
    for tweet in tweets:
        sum += 1
        if "media" in tweet.entities:
            pic += 1
            for tweet_media in tweet.entities["media"]:
                url = tweet_media["media_url_https"]
                download(url, search_str)
                print(pic, "/", sum, url)

def download(url, search_str):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(".\\image")
    if not os.path.exists(search_str):
        os.mkdir(search_str)

    path = os.path.join(search_str, url.split('/')[-1])
    url += ":orig"

    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print("Error")

def main():
    t1 = time.time()

    search_str = set_search_str()
    search(search_str)

    t2 = time.time()
    print(t2 - t1, "sec")

if __name__ == '__main__':
    main()