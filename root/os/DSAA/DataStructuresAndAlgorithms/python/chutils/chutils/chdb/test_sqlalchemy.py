#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_sqlalchemy.py
# chdb
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 03/07/19 14:37.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
SQLAlchemy
"""
from sqlalchemy import (
        Column, String, BigInteger, Integer, CHAR, VARCHAR, create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类
Base = declarative_base()


# 定义Student对象
class Student(Base):
    # 表的名称
    __tablename__ = 'student'

    # 表的结构
    id = Column(BigInteger, primary_key=True)
    name = Column(String(20))
    class_id = Column(BigInteger)
    gender = Column(CHAR)
    age = Column(Integer)
    id_card = Column(BigInteger)


# 定义班级对象
class Class(Base):
    # 表的名称
    __tablename__ = 'class'

    # 表的结构
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(30))


# 初始化数据库连接
engine = create_engine(
        'mysql+mysqlconnector://user:password@localhost:3306/test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建新Student对象:
new_student = Student(
        id=100, name='Chyi Yaqing', class_id=1105,
        gender='M', age=26, id_card='410526')

# 添加到session:
# session.add(new_student)

# 提交即保存到数据库
# session.commit()

# 查询数据
# 创建Query查询，filter是where条件，最后调用one()返回惟一行，如果调用all()返回所有行
student = session.query(Student).filter(Student.id == 100).one()

# 打印类型和对象
print('Type: %s, id=%s, name=%s' % (type(student), student.id, student.name))

# 关闭session
session.close()
