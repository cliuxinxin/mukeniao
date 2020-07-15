import hashlib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqllayer import Data

# 创建对象的基类:
Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/data')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()


# Generate MD5
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

# read the data and clean a little
with open('data/test.txt','r') as f:
    data = f.read().replace('\n', '').replace('\r', '').replace(' ', '').replace('u30000', '').strip()

# chage data to list
data = data.split('。')

with open('data/test_clean.txt','w') as f:
    for i,entry in enumerate(data):
        f.write(entry)
        f.write('\n')
        new_data = Data(md5=md5(entry),id=i,datasource='test_clean.txt')
        session.merge(new_data)
        session.commit()

session.close()
print('test')