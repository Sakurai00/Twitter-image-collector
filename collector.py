import tweepy, os, urllib, time
import settings as st

auth = tweepy.OAuthHandler(st.CONSUMER_KEY, st.CONSUMER_SECRET)
auth.set_access_token(st.ACCESS_TOKEN_KEY, st.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def search():
    sum = 1
    pic = 0
    search_str = st.TARGET_WORD + "exclude:retweets"
    tweets = tweepy.Cursor(api.search, q = search_str).items(st.SEARCH_NUM)
    for tweet in tweets:
        sum += 1
        if "media" in tweet.entities:
            pic += 1
            for tweet_media in tweet.entities["media"]:
                url = tweet_media["media_url_https"]
                download(url)
                print(pic, "/", sum, url)

def download(url):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(".\\image")
    if not os.path.exists(st.TARGET_WORD):
        os.mkdir(st.TARGET_WORD)

    path = os.path.join(st.TARGET_WORD, url.split('/')[-1])
    url += ":orig"

    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        pass

def main():
    t1 = time.time()
    search()
    t2 = time.time()
    print(t2 - t1, "sec")

if __name__ == '__main__':
    main()