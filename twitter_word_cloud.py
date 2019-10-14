from datetime import datetime

import matplotlib.pyplot as plt
import nagisa
from wordcloud import WordCloud

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
    words = sum([nagisa.extract(r.text, extract_postags=["名詞"]).words for r in result], [])
    without_num = [w for w in words if not w.isdigit()]

    cloud = WordCloud().generate(" ".join(without_num))

    plt.figure()
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
