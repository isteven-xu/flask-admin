#-*- coding:utf-8 -*-
from flask import Blueprint,redirect,render_template,url_for,flash
from flask_login import logout_user,login_user,current_user
from .forms import LoginForm
from ..user.models import User

auth = Blueprint('auth',__name__,static_folder='../static')

@auth.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return  redirect(url_for('main.index'))

    form  = LoginForm()
    #import pdb;pdb.set_trace()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        u=User.query.filter(User.username == username).first()
        print u
        if u is not None :
            if u.verify_passowrd(password):
                login_user(u)
                return redirect(url_for('main.index'))
            else:
                flash(u'密码错误',category='info')
        else:
            flash(u'用户名不存在',category='info')
    return render_template('login.html',form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))