from datetime import datetime
from pymongo import MongoClient
from umongo import Instance, Document, fields, validate


db = MongoClient().test
instance = Instance(db)


@instance.register
class CafeEmployee(Document):
    username = fields.StringField(required=True, unique=True, validate=[validate.Length(min=6),
                                                                        validate.Length(max=60),
                                                                        validate.Regexp(r"[a-zA-Z ']+")])
    password = fields.StringField(required=True, unique=True, validate=[validate.Length(min=8),
                                                                        validate.Length(max=100),
                                                                        validate.Regexp(r"[a-zA-Z0-9 ']+")])
    id_cafe = fields.ReferenceField(Cafe)  #fields.ObjectIdField
    # group = fields.IntegerField()
    token = fields.StringField(required=True)

    class Meta:
        collection = db.employee


@instance.register
class PaymentTypes(Document):
    name = fields.StringField(required=True, unique=True)

    class Meta:
        collection = db.paymenttypes


@instance.register
class Cafe(Document):
    # id_cafe = fields.IntegerField()
    name_cafe = fields.StringField(required=True, unique=True)
    address = fields.StringField(required=True, unique=True)
    info = fields.StringField()
    image_url_cafe = fields.UrlField()
    payment_type = fields.ReferenceField(PaymentTypes)

    class Meta:
        collection = db.cafe


@instance.register
class Category(Document):
    # id_cat = fields.IntegerField()
    id_cafe = fields.ReferenceField(Cafe)
    name_cat = fields.StringField(required=True, unique=True)
    image_url_cat = fields.UrlField()

    class Meta:
        collection = db.category

@instance.register
class Product(Document):
    # id_prod = fields.IntegerField()
    id_cat = fields.ReferenceField(Category)
    name_prod = fields.StringField(required=True, unique=True)
    description = fields.StringField(required=True, unique=True)
    price = fields.NumberField(required=True)
    image_url_prod = fields.UrlField()
    avail_from = fields.DateTimeField()
    avail_till = fields.DateTimeField()

    class Meta:
        collection = db.product


@instance.register
class Order(Document):
    id_order = fields.IntegerField(required=True, unique=True)
    products = fields.ListField(fields.ReferenceField(Product))
    user_id = fields.IntegerField(required=True, unique=True)
    order_dtime = fields.DateTimeField()
    del_dtime = fields.DateTimeField()

    class Meta:
        collection = db.order


@instance.register
class Payment(Document):
    id_order = fields.ReferenceField(Order)
    status = fields.BooleanField()
    del_dtime = fields.DateTimeField()

    class Meta:
        collection = db.employee


# vegeta = User(email='vegeta@over9000.com', friends=[goku])
# vegeta.commit() #add to db
#
# vegeta.dump() #serialization
