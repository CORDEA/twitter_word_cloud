from datetime import datetime

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
    texts = [m.text for m in result]
    print(texts)


if __name__ == "__main__":
    main()
