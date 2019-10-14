import twitter


class TwitterClient:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.api = twitter.Api(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )

    def search(self, term, since, until):
        return self.api.GetSearch(term=term, until=until, since=since)
