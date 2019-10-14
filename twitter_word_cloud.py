import sys

import matplotlib.pyplot as plt
import nagisa
from wordcloud import WordCloud

import settings
from twitter_client import TwitterClient


def main():
    query = sys.argv[1]
    since, until = sys.argv[2].split("..")

    client = TwitterClient(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        access_token_key=settings.ACCESS_TOKEN_KEY,
        access_token_secret=settings.ACCESS_TOKEN_SECRET
    )
    result = client.search(query, since, until)
    words = sum([nagisa.extract(r.text, extract_postags=["名詞"]).words for r in result], [])
    lower_query = query.lower()
    without_num = [w for w in words if not w.isdigit() and not w.lower() == lower_query]

    cloud = WordCloud(
        background_color="white",
        contour_width=5,
        contour_color="royalblue"
    ).generate(" ".join(without_num))

    plt.figure()
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
