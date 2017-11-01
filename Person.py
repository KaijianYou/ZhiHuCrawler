class Person(object):
    def __init__(self, name, url, avatar, bio, followings, followers, asks, answers):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def to_dict(self):
        for k, v in locals().items():
            if k != self and v is None:
                locals()[k] = v

        return dict(name=self.name,
                    url=self.url,
                    avatar=self.avatar,
                    bio=self.bio,
                    followings=self.followings,
                    followers=self.followers,
                    asks=self.asks,
                    answers=self.answers)

