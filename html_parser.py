# -*- coding: utf-8 -*-


import re

from Person import Person
from bs4 import BeautifulSoup


user_profile_url = 'https://www.zhihu.com/people/'


class HTMLParser(object):
    """HTML 分析器"""
    def __init__(self):
        pass

    def _get_next_urls(self, html_page):
        followings = []
        m = re.search(r'followingByUser.*?ids":\[(.*?),null', html_page)
        if m is not None:
            following_user_list = m.group(1).split(',')
            following_user_list = [user[1:-1] for user in following_user_list]
            followings.extend(following_user_list)

        next_urls = []
        for following in followings:
            user_url = user_profile_url + following
            user_url += 'following' if user_url[-1] == '/' else '/following'
            next_urls.append(user_url)
        return next_urls

    def _get_data(self, page_url, soup):
        try:
            name = soup.find('span', class_='ProfileHeader-name').text
        except AttributeError:
            return None

        avatar = soup.select('div.UserAvatar > img.Avatar')[0].get('src')
        bio_tag = soup.find('span', 'ProfileHeader-headline')
        bio = bio_tag.text if bio_tag is not None else ''

        following_num, follower_num = '', ''
        followship_tags = soup.select('div.FollowshipCard-counts > a')
        for followship_tag in followship_tags:
            if followship_tag.select('div.NumberBoard-name')[0].text == u'关注了':
                following_num = followship_tag \
                    .find('div', class_='NumberBoard-value').text
            if followship_tag.select('div.NumberBoard-name')[0].text == u'关注者':
                follower_num = followship_tag \
                    .find('div', class_='NumberBoard-value').text

        ask_num, answer_num = '', ''
        profile_tags = soup.select('div.ProfileMain-header > ul > li')
        for profile_tag in profile_tags:
            if profile_tag.get('aria-controls') == 'Profile-answers':
                answer_num = profile_tag.find('span').text
                continue
            if profile_tag.get('aria-controls') == 'Profile-asks':
                ask_num = profile_tag.find('span').text

        person = Person(name=name, url=page_url, avatar=avatar, bio=bio,
                        followings=following_num, followers=follower_num,
                        asks=ask_num, answers=answer_num)
        data = {name: person.to_dict()}
        return data

    def parse(self, page_url, html_page):
        if page_url is None or html_page is None:
            return None, None
        soup = BeautifulSoup(html_page, 'lxml', from_encoding='utf-8')

        data = self._get_data(page_url, soup)
        if data is None:
            return None, None

        next_urls = self._get_next_urls(html_page)
        return next_urls, data


if __name__ == '__main__':
    pass
