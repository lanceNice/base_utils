# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 11:00
# @Author  : lance
# @File    : idcard_utils.py
# @Software: PyCharm
import logging
import datetime
import time


#  身份证操作相关工具类
class IdCardUtils(object):

    def __init__(self, id):
        self.id = id

    def verity_id(self):
        """
        身份证校验
        :param id_card:
        :return:合法：1不合法：0
        """
        try:
            sfz = self.id.strip().upper()
            if len(sfz) == 18:
                value_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
                ret_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
                start_2 = int(sfz[:2])
                birthday = sfz[6:14]
                date = birthday[:4]
                if start_2 > 10 and int(date) > 1900:
                    time.strptime(birthday, '%Y%m%d')
                    sum = 0
                    for i in range(17):
                        sum += int(sfz[i]) * value_list[i]
                    ys = sum % 11
                    if ret_list[ys] == sfz[17]:
                        return 1
        except Exception as e:
            print(e)
            return 0
        return 0

    def get_birthday(self):
        """
        通过身份证号获取出生日期
        返回data类型
        """
        birth_year = int(self.id[6:10])
        birth_month = int(self.id[10:12])
        birth_day = int(self.id[12:14])
        birthday = "{0}-{1}-{2}".format(birth_year, birth_month, birth_day)
        array = birthday.split('-')
        month = int(birthday.split('-')[1])
        if month < 10:
            month_str = '0' + str(month)
            array[1] = month_str
            res = '-'.join(array)
        else:
            res = birthday
        return res

    def get_sex(self):
        """男生：0 女生：1"""
        num = int(self.id[16:17])
        if num % 2 == 0:
            return 1
        else:
            return 0

    def get_age(self):
        """通过身份证号获取年龄"""
        birth_year = int(self.id[6:10])
        birth_month = int(self.id[10:12])
        birth_day = int(self.id[12:14])
        now = (datetime.datetime.now() + datetime.timedelta(days=1))
        year = now.year
        month = now.month
        day = now.day

        if year == birth_year:
            return 0
        else:
            if birth_month > month or (birth_month == month and birth_day > day):
                return year - birth_year - 1
            else:
                return year - birth_year


if __name__ == '__main__':
    id = '41142119941104721X'
    idcard_utils = IdCardUtils(id)
    birthday = idcard_utils.get_birthday()
    print(birthday)
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    print(birthday)
    print(idcard_utils.verity_id())
