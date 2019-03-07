#-*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length



class LoginForm(FlaskForm):
    username = StringField(u'用户', validators=[DataRequired(message=u'用户名不能为空'), Length(1, 20,message=u'长度为1-20')])
    password = PasswordField(u'密码', validators=[DataRequired(message=u'密码不能为空'), Length(1, 32,message=u'密码长度为1-32')])
    submit = SubmitField(u'登录')