# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 15:23
# @Author  : lance
# @File    : random_str.py
# @Software: PyCharm
# 随机数
import datetime
import struct
from random import Random

from bson import ObjectId


# 唯一值生成
def get_uuid():
    """
    :return: 201907180946536922236835
    """
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + \
           '%.10d' % int(str(struct.unpack('>Q', ObjectId().binary[-8:])[0])[-10:])


# 随机数生成器
def random_str(randomlength=8):
    """
    :param randomlength: 位数
    :return:
    """
    string = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789~!@#$%^&*'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        string += chars[random.randint(0, length - 1)]
    return string


if __name__ == '__main__':
    print(get_uuid())
    pass
