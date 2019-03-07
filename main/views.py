#-*-coding:utf-8-*-
from flask import Blueprint,render_template,redirect,url_for,jsonify,request
from flask_login import current_user,login_required
from ..dim.models import Dimension, DimLkpProductCatagory, DimLkpPayMode
from ..extensions import db

main = Blueprint('main',__name__,static_folder='../static')

def dimdb(table_name):
    if table_name == 'Dimension':
        return Dimension
    elif table_name == 'DimLkpProductCatagory':
        return DimLkpProductCatagory
    elif table_name == 'DimLkpPayMode':
        return DimLkpPayMode



@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))


@main.route('/jobs')
@login_required
def job_home():
    return render_template('job/home.html')

@main.route('/dims')
@login_required
def dim_home():
    return render_template('dim/home.html')


@main.route('/dims/getData',methods=['GET'])
@login_required
def dim_list():
    offset = request.args['offset']
    limit = request.args['limit']
    name = request.args['name']
    desc = request.args['desc']
    table_name = request.args['tablename']
    print name
    table = dimdb(table_name)
    dims_query = table.query\
                    .filter(table.key_person.like('%'+ name + '%') if name else '' )\
                    .filter(table.description.like('%' + desc + '%') if desc else '')

    dims=dims_query.limit(limit).offset(offset).all()

    result = []
    total = len(dims_query.all())
    for dim in dims:
        result.append(dim.to_dict())
    return jsonify({'total':total,'rows':result}),200

@main.route('/dims/add',methods=['POST'])
@login_required
def dim_add():
    exchange_data = eval(request.form.get('exchange_data'))
    table_name = request.form.get('tablename')
    table = dimdb(table_name)
    dim = table(**exchange_data)
    db.session.add(dim)
    db.session.commit()
    return jsonify({'message': u'添加成功'})

@main.route('/dims/edit',methods=['POST'])
@login_required
def dim_edit():
    id = request.form.get('id')
    exchange_data = eval(request.form.get('exchange_data'))
    table_name = request.form.get('tablename')
    print exchange_data
    table = dimdb(table_name)

    table.query.filter(table.id == id).update(exchange_data)
    db.session.commit()
    return jsonify({'message':u'修改成功'})

@main.route('/dims/delete',methods=['POST'])
@login_required
def dim_delete():
    id = request.form.get('id')
    table_name = request.form.get('tablename')

    table = dimdb(table_name)

    table.query.filter(table.id == id).delete()
    db.session.commit()
    return jsonify({'message': u'删除成功'})

@main.route('/dims/<name>',methods=['GET','POST'])
@login_required
def dim_item(name):
    print name
    print type(name)
    table_name = name[name.find('_', 2) + 1:]
    print table_name
    table_url = 'dim/' + table_name + '.html'
    print table_url
    return render_template(table_url)

@main.route('/dims/test',methods=['GET'])
@login_required
def dim_test():
    return render_template('dim/dim_lkp_product_catagory.html')


@main.route('/dims/getData/dim_lkp_product_catagory', methods=['GET'])
@login_required
def dim_product_catagory_list():
    offset = request.args['offset']
    limit = request.args['limit']
    pay_channel_code = request.args['channelcode']
    biz_prod_code = request.args['productcode']
    table_name = request.args['tablename']
    table = dimdb(table_name)
    dims_query = table.query\
                    .filter(table.pay_channel_code == pay_channel_code if pay_channel_code else '' )\
                    .filter(table.biz_prod_code == biz_prod_code if biz_prod_code else '')

    dims=dims_query.limit(limit).offset(offset).all()

    result = []
    total = len(dims_query.all())
    for dim in dims:
        result.append(dim.to_dict())
    return jsonify({'total':total,'rows':result}),200
