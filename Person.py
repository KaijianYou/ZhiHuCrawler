# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, url, avatar, bio, followings, followers, asks, answers):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        # self.name = name,
        # self.url = url,
        # self.avatar = avatar,
        # self.bio = bio,
        # self.followings = followings,
        # self.followers = followers,
        # self.asks = asks,
        # self.answers = answers

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


if __name__ == '__main__':
    pass
