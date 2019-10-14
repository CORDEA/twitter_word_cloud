from datetime import datetime

import nagisa

import settings
from twitter_client import TwitterClient


def main():
    client = TwitterClient(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        access_token_key=settings.ACCESS_TOKEN_KEY,
        access_token_secret=settings.ACCESS_TOKEN_SECRET
    )
    result = client.search("", datetime.now(), datetime.now())
    words = sum([nagisa.extract(r, extract_postags=["名詞"]).words for r in result], [])
    without_num = [w for w in words if not w.isdigit()]


if __name__ == "__main__":
    main()
