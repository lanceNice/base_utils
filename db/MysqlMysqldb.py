# MySQLdb
import MySQLdb

# 连接数据
def connect_mysql(db_host="127.0.0.1", user="root",passwd="root",db="scrapy_spider", charset="utf8"):
    conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
    conn.autocommit(True)
    return conn.cursor()

#查询
def do1():
    sql = ('SELECT * from article limit 10')
    db1 = connect_mysql()
    db1.execute(sql)
    for row in db1:
        print(*row)

# 多数据插入
def do2():
    sql = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (18684928,18684928,"内蒙古赤峰市巴林左旗","联通林东镇新城区BRAS数据机房")'
    sql_tmp = 'INSERT INTO `ipdata` (`startip`,`endip`,`country`,`local`) VALUES (%s, %s, %s, %s)'
    values = [(16890112, 16891391, "泰国", "曼谷"), (16891392, 16891647, "泰国", "如果硅农"), (16891648, 16892159, "泰国", "加拉信府")]
    db1 = connect_mysql()
    print(db1.execute(sql), db1.lastrowid)
    print(db1.executemany(sql_tmp, values), db1.lastrowid)



if __name__ == '__main__':
    do1()

