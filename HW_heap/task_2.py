import heapq


class Twitter:
    """Упрощённая версия Twitter."""

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        self.tweets.setdefault(userId, []).append(
            (self.time, tweetId)
        )

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        authors = set(self.following.get(userId, set()))
        authors.add(userId)

        for authorId in authors:
            author_tweets = self.tweets.get(authorId, [])

            if not author_tweets:
                continue

            index = len(author_tweets) - 1
            timestamp, tweetId = author_tweets[index]

            heapq.heappush(
                heap,
                (-timestamp, tweetId, authorId, index)
            )

        feed = []

        while heap and len(feed) < 10:
            _, tweetId, authorId, index = heapq.heappop(heap)

            feed.append(tweetId)

            if index > 0:
                previous_index = index - 1

                timestamp, previous_tweetId = (
                    self.tweets[authorId][previous_index]
                )

                heapq.heappush(
                    heap,
                    (
                        -timestamp,
                        previous_tweetId,
                        authorId,
                        previous_index,
                    )
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(
            followerId,
            set()
        ).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
