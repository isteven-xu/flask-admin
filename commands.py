from user.models import User
import click
from flask.cli import with_appcontext
from extensions import db
from user.models import User


@click.command()
@click.option('-u','--username',prompt=True)
@click.option('-p','--password',prompt=True)
@with_appcontext
def create_user(username,password):
    u = User.query.filter(User.username == username).first()
    if u is not None :
        print('User already exist!')
    else:
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        print('User added successful.')
