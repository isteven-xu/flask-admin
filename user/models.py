#-*- coding:utf-8 -*-
from ..extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=True, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError(u'密码不允许读取！')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_passowrd(self,password):
        return check_password_hash(self.password_hash,password)
