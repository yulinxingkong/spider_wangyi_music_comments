import random
import time

import requests


# header = {}

def firs_request(url):
    r = requests.get(url)
    content = r.json()
    # 调用解析热门评论
    parser_hot_comments(content)
    # 调用普通解析函数
    parser_content(content)
    total_comment = content['total']
    return total_comment


def after_request(total_comment, url_template, song_id):
    # if total_comment % 20:
    #     # 余数不为零,
    #     page = total_comment//20 +1
    # else:
    #     # 余数为零
    #     page = total_comment // 20
    page = total_comment // 20 + 1 if total_comment % 20 else total_comment // 20
    print(page)
    # 构造url 列表请求
    # for i in range(2, page):
    for i in range(2, 5):  # 测试
        time.sleep(random.choice([1, 2, 3, 0.5]))
        url = url_template.format(song_id, (i - 1) * 20)
        r = requests.get(url)
        content = r.json()
        parser_content(content)
    # return page


def parser_content(content):
    """
    解析普通评论
    :param content: json() 后的内容
    :return:
    """
    content = content["comments"]  # 热门评论
    for i in content:
        print(i["content"])  # 评论内容
        print(i["likedCount"], '普通点赞数量')  # 点赞数量
        print(i['user']['userId'])  # 评论人id


def parser_hot_comments(content):
    """
    解析热门评论
    :param content:
    :return:
    """
    content = content["hotComments"]  # 热门评论
    for i in content:
        print(i["content"])  # 评论内容
        print(i["likedCount"], '热门点赞数量')  # 点赞数量
        print(i['user']['userId'])  # 评论人id


if __name__ == '__main__':
    url_template = 'https://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=20&offset={}'  # 歌曲id
    # song_id = '553534113'  # 赵雷的 画
    # song_id = '202369'  # 赵雷的 画
    song_id = '569200213'  # 毛不易 消愁
    total_comment = firs_request(url_template.format(song_id, 0))
    print(total_comment)
    after_request(total_comment, url_template, song_id)

    # 第一次请求获取, 有多少条数据  total   第一次有请求有热门评论, 后面没有
    # 根据有多少条数据 构造 url 列表 逐个请求,
