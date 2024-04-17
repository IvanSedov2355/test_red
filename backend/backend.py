import atexit
import os
import datetime
import re
import uuid
from typing import Union

import pydantic
from flask import Flask, jsonify, request, render_template
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

path = os.path.join(os.getcwd(), 'reg_data.db')


backend_app = Flask(__name__)
bcrypt = Bcrypt(backend_app)
engine = create_engine('sqlite:///'+f"{path}")
Base = declarative_base()
Session = sessionmaker(bind=engine)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    soname = Column(String(100))
    name = Column(String(100))
    soname_name = Column(String(200))
    birthday = Column(String(200))
    country = Column(String(200))
    lager = Column(String(200))
    children_count = Column(String(200))
    contact_data = Column(String(200))
    registration_time = Column(DateTime, server_default=func.now())


class Stories(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    soname_name = Column(String(1000))
    birthday = Column(String(200))
    lager = Column(String(200))
    stories_ = Column(String(2000000000000000000))
    registration_time = Column(DateTime, server_default=func.now())

Base.metadata.create_all(engine)
atexit.register(lambda: engine.dispose())

@backend_app.route('/')
def index():
    return render_template('index.html')

@backend_app.route('/registration')
def registration():
    return render_template('form_registration.html')


@backend_app.route('/about')
def about():
    return render_template('about.html')

@backend_app.route('/stories')
def stories():
    return render_template('stories about you.html')

@backend_app.route('/result')
def result():
    return render_template('results.html')

@backend_app.route("/send_data_form", methods=["POST"], endpoint="send_data_form")
def login():
    login_data = request.form
    user = User(soname=login_data['soname'], name=login_data['name'],
                birthday=login_data['date'], country=login_data['country'], lager=login_data['lager'],
                children_count=login_data['child'], contact_data=login_data['username'])
    with Session() as sessions:
        sessions.add(user)
        sessions.commit()
    return render_template('answer_registration.html')

@backend_app.route("/send_stories", methods=["POST"], endpoint="send_stories")
def stories():
    login_data_ = request.form
    stories_ = Stories(soname_name=login_data_['soname'], birthday=login_data_['date'], lager=login_data_['lager'],
            stories_=login_data_['stories_'])
    with Session() as sessions:
        sessions.add(stories_)
        sessions.commit()
    return render_template('answer_registration.html')



if __name__ == '__main__':
    backend_app.run(
        host='0.0.0.0',
        port=80
    )