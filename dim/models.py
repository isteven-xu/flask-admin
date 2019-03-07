from ..extensions import db

class Dimension(db.Model):
    __tablename__ = 'dimension'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    key_person = db.Column(db.String(64), nullable=True, unique=False)
    description = db.Column(db.String(255), nullable=True, unique=False)

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict

class DimLkpProductCatagory(db.Model):
    __tablename__ = 'dim_lkp_product_catagory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    catagory_v1 = db.Column(db.String(64), nullable=False, unique=False)
    catagory_v2 = db.Column(db.String(64), nullable=False, unique=False)
    catagory_v3 = db.Column(db.String(64), nullable=True, unique=False)
    catagory_v4 = db.Column(db.String(64), nullable=True, unique=False)
    catagory_v5 = db.Column(db.String(64), nullable=True, unique=False)
    catagory_v6 = db.Column(db.String(64), nullable=True, unique=False)
    pay_channel_code = db.Column(db.String(64), nullable=False, unique=False)
    pay_channel_name = db.Column(db.String(64), nullable=False, unique=False)
    biz_prod_code = db.Column(db.String(64), nullable=False, unique=False)
    biz_prod_name = db.Column(db.String(64), nullable=False, unique=False)

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict


class DimLkpPayMode(db.Model):
    __tablename__ = 'dim_lkp_pay_mode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pay_mode = db.Column(db.String(64), nullable=False, unique=False)
    status = db.Column(db.String(2), nullable=True, unique=False)
    show_level = db.Column(db.String(2), nullable=True, unique=False)
    gmt_create = db.Column(db.Date, nullable=False, unique=False)
    gmt_modified = db.Column(db.Date, nullable=False, unique=False)
    remark = db.Column(db.String(512), nullable=False, unique=False)
    extension = db.Column(db.String(2000), nullable=True, unique=False)
    dw_create_time = db.Column(db.Date, nullable=False, unique=False)
    dw_modified_time = db.Column(db.Date, nullable=False, unique=False)
    category = db.Column(db.String(64), nullable=False, unique=False)

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict

