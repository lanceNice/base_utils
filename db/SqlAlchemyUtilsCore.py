import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///foo.db', echo=True)

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
  Column('id', Integer, primary_key=True),
  Column('user_id', None, ForeignKey('users.id')),
  Column('email_address', String, nullable=False)
)

# metadata.create_all(engine)
conn = engine.connect()

# conn.execute(users.insert(), [dict(name='jack', fullname='Jack Jones'),
#                               dict(name='wendy', fullname='Wendy Williams')])
# conn.execute(addresses.insert(), [
#    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
#    {'user_id': 1, 'email_address' : 'jack@msn.com'},
#    {'user_id': 2, 'email_address' : 'www@www.org'},
#    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
# ])

from sqlalchemy.sql import select
# s = select([users])
# result = conn.execute(s)
# for row in result:
#     print(row)

# s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
# for row in conn.execute(s):
#     print row


from sqlalchemy.sql import text
s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
        "AND users.name BETWEEN :x AND :y "
        "AND (addresses.email_address LIKE :e1 "
            "OR addresses.email_address LIKE :e2)")
print(conn.execute(s, x='m', y='z', e1='%@aol.com', e2='%@msn.com').fetchall())