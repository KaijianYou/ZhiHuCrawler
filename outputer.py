# -*- coding: utf-8 -*-


import json
import codecs


class Outputer(object):
    """数据采集、分析、输出器"""
    def __init__(self):
        self._datas = {}

    def collect_data(self, data):
        if data is None:
            return
        self._datas.update(data)

    def output_html(self):
        """以 HTML 格式写数据到文件"""
        if self._datas:
            with codecs.open('user_data.html', 'w', encoding='utf-8') as f:
                f.write('<html>')
                f.write('<head>')
                f.write('<meta http-equiv="content-type" '
                        'content="text/html;charset=utf-8">')
                f.write('<style type="text/css">')
                f.write('table { border-spacing: none; border-collapse: collapse; }')
                f.write('table td { border: 1px solid #dedede; }')
                f.write('</style>')
                f.write('</head>')
                f.write('<body>')
                f.write('<table>')
                f.write('<thead>')

                f.write(u'<td>用户名</td>')
                f.write(u'<td>域名</td>')
                f.write(u'<td>简介</td>')
                f.write(u'<td>头像 URL</td>')
                f.write(u'<td>关注者</td>')
                f.write(u'<td>关注了</td>')
                f.write(u'<td>回答数</td>')
                f.write(u'<td>提问数</td>')

                # f.write('<td>User Name</td>')
                # f.write('<td>URL</td>')
                # f.write('<td>Bio</td>')
                # f.write('<td>Avatar URL</td>')
                # f.write('<td>Followers</td>')
                # f.write('<td>Followings</td>')
                # f.write('<td>Answers</td>')
                # f.write('<td>Asks</td>')

                f.write('</thead>')
                f.write('<tbody>')
                for k, v in self._datas.items():
                    f.write('<tr>')
                    f.write('<td>%s</td>' % k)
                    f.write('<td>%s</td>' % v['url'])
                    f.write('<td>%s</td>' % v['bio'])
                    f.write('<td>%s</td>' % v['avatar'])
                    f.write('<td>%s</td>' % v['followers'])
                    f.write('<td>%s</td>' % v['followings'])
                    f.write('<td>%s</td>' % v['answers'])
                    f.write('<td>%s</td>' % v['asks'])
                    f.write('</tr>')
                f.write('</tbody')
                f.write('</table>')
                f.write('</body>')
                f.write('</html>')
            print('Write to html done.')
        else:
            print('No data')

    def output_json(self):
        """以 json 格式写数据到文件"""
        if self._datas:
            with codecs.open('user_data.txt', 'w', encoding='utf-8') as f:
                json.dump(self._datas, f, indent=4, skipkeys=True, ensure_ascii=False)
            print('Write to json done.')
        else:
            print('No data')

    def data_profiler(self):
        """数据分析"""
        with codecs.open('user_data.txt', encoding='utf-8') as f:
            data = json.load(f)

        persons = data.values()
        scale = [0, 10, 50, 100, 200, 500, 1000, 3000, 5000,
                 10000, 100000, 1000000, 10000000]

        numbers = []
        for i in range(len(scale) - 1):
            numbers.append(len([person for person in persons if scale[i] <=
                                int(person["followers"]) < scale[i + 1]]))

        print('range        ', scale)
        print('user numbers ', numbers)
        print('percentage   ', [round(float(number) * 100 / sum(numbers), 2)
                               for number in numbers])


if __name__ == '__main__':
    pass

