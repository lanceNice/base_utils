import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import and_, or_

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/scrapy_spider', echo=True)
Base = declarative_base()

class Student(Base):
        __tablename__ = 'student'
        id = Column(Integer, primary_key=True)
        name = Column(String(40))
        age = Column(String(40))
        height = Column(String(40))

        def __repr__(self):
            return "<Student(name='%s', age='%s', height='%s')>" % (
                self.name, self.age, self.height)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    fullname = Column(String(40))
    password = Column(String(40))
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('addresses', order_by=id))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

def createTable():
    Base.metadata.create_all(engine)
    pass

def insert():
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])

    jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
    jack.addresses = [Address(email_address='jack@google.com'), Address(email_address='j25@yahoo.com')]
    session.add(jack)

    session.commit()
    pass

def delete():
    pass

def update():
    pass

def select():
    Session = sessionmaker(bind=engine)
    session = Session()
    # 单条查询
    our_user = session.query(User).filter_by(name='ed').first()

    # 查询全部
    all_user= session.query(User).all()

    # 查询个数
    print(session.query(User).filter(User.name == 'ed').count())

    # for row in session.query(User).order_by(User.id):
    #     print(row)
    #
    # for row in session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack'])):
    #     print(row)
    # for row in session.query(User).filter(~User.name.in_(['ed', 'wendy', 'jack'])):
    #     print(row)
    #
    # for row in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
    #     print(row)
    #
    # for row in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
    #     print(row)


    # for u, a in session.query(User, Address).\
    #                     filter(User.id==Address.user_id).\
    #                     filter(Address.email_address=='jack@google.com').\
    #                     all():
    #     print u, a

if __name__ == '__main__':
    print(sqlalchemy.__version__)
    createTable()
    #insert()
    #select()
    pass
