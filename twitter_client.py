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
        all_result = set()
        min_id = None
        while True:
            result = self.api.GetSearch(term=term, until=until, since=since,
                                        count=100, result_type="recent", max_id=min_id)
            new_min_id = min([r.id for r in result])
            if min_id == new_min_id:
                break
            else:
                all_result.update(result)
                min_id = new_min_id
        return [t for t in all_result if t.retweeted_status is None]
