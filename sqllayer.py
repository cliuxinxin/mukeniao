# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    last_name = Column(String(20))

class Data(Base):
    # 表的名字:
    __tablename__ = 'data'

    # 表的结构:
    md5 = Column(String(40), primary_key=True)
    id = Column(String(20))
    datasource = Column(String(20))


if __name__ == "__main__":
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/data')

    # 新建表格
    Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='5', name='ablert')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    try:
        session.commit()
    except:
        pass
    # 关闭session:
    session.close()