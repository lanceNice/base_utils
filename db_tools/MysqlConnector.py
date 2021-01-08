# mysql-connector-python
from mysql import connector

#查询
def do1():
    conn = connector.Connect(host="127.0.0.1", user="root",password="root", database="scrapy_spider", charset="utf8")
    conn.autocommit = True
    db0 = conn.cursor()
    sql = ('SELECT * from article limit 10')
    db0.execute(sql)
    for row in db0:
        print(*row)
    conn.close()


# 多数据插入
def do2():
    conn = connector.Connect(host="127.0.0.1", user="root", password="root", database="scrapy_spider", charset="utf8")
    conn.autocommit = True
    sql = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (18684928,18684928,"内蒙古赤峰市巴林左旗","联通林东镇新城区BRAS数据机房")'
    sql_tmp = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (%s, %s, %s, %s)'
    values = [(16890112,16891391,"泰国","曼谷"),(16891392,16891647,"泰国","如果硅农"), (16891648,16892159,"泰国","加拉信府")]
    db0 = conn.cursor()
    print (db0.execute(sql))
    print (db0.executemany(sql_tmp, values))
    conn.close()



if __name__ == '__main__':
    do1()
    pass

