from datetime import datetime
from pymongo import MongoClient
from umongo import Instance, Document, fields
from umongo.validate import Length
from hashlib import sha256

db = MongoClient().cafe_name
instance = Instance(db)


"""
Íå íóæíî ïðîïèñûâàòü â Ìåòå ÿâíî íàçâàíèå òàáëèöû, ôðåéìâîðê ñàì åãî ñôîðìèðóåò
Ïðîâåðêè íà ðåãåêñï òîæå íå íàäî. Ìîíãà ñúåñò ëþáûå äàííûå, ýòî íå ïëþñû, ãäå
ìîãóò áûòü ïðîáëåìû.

Åñëè ñ ôèëäàìè åñòü ñìûñë èìïîðòèòü fields, ïîòîìó ÷òî èõ ìíîãî, òî ïàêåòû òèïà
validate - íåò, òàì òåáå íóæíû 1-2 ìåòîäà/êëàññà, ïîýòîìó åñòü ñìûñë îïòèìèçèðîâàòü
èìïîðòû.

Íàçûâàé ïîëÿ, êîòîðûå ññûëàþòñÿ íà äðóãèå äîêóìåíòû, áåç ïðèñòàâêè id. Îíî è ïðèÿòíåå
ãëàçó, è ïî ñìûñëó ïðàâèëüíåå.

Ïàðîëü íå äîëæåí õðàíèòüñÿ â îòêðûòîì âèäå, íóæíà ôóíêöèÿ øèôðîâàíèÿ, õîòÿ áû ñàìàÿ ïðîñòàÿ
sha256.
Ïàðîëè íå íóæíî âàëèäèðîâàòü íà óðîâíå äîêóìåíòà, ýòî äîëæåí äåëàòü ôðîíò.
?? âîîáùå âàëèäàöèåé çàíèìàþòñÿ ñåðèàëàéçåðû, òóò óäîáíåå þçàòü Marshmallow.

Íå ñîêðàùàé íàçââàíèÿ 'category' -> 'cat' â óãîäó ñêîðîñòè. Êîä äîëæåí áûòü ÷èòàåìûì
äàæå íà óðîâíå âîò òàêîãî ñìûñëà.
"""


@instance.register
class PaymentType(Document):
    name = fields.StringField(required=True, unique=True)


@instance.register
class Cafe(Document):
    name = fields.StringField(required=True, unique=True)
    addresses = fields.StringField(required=True)
    info = fields.StringField()
    image_url = fields.UrlField()
    payment_type = fields.ReferenceField(PaymentType)


@instance.register
class CafeEmployee(Document):
    username = fields.StringField(required=True, unique=True, validate=[Length(min=6, max=60)])
    password = fields.StringField(required=True)
    cafe = fields.ReferenceField(Cafe)  # fields.ObjectIdField
    # group = fields.IntegerField()
    token = fields.StringField(required=True)

    def hash_password(self):
        self.password = sha256(self.password.encode('UTF-8') + self.username.encode('UTF-8')).hexdigest()
    # pass
    # return sha256(data)


@instance.register
class Category(Document):
    cafe = fields.ReferenceField(Cafe)
    name = fields.StringField(required=True, unique=True)
    image_url = fields.UrlField()


@instance.register
class Product(Document):
    category = fields.ReferenceField(Category)
    name = fields.StringField(required=True, unique=True)
    description = fields.StringField(required=True, unique=True)
    price = fields.NumberField(required=True)
    image_url = fields.UrlField()
    available_from = fields.DateTimeField()
    available_till = fields.DateTimeField()


@instance.register
class Order(Document):
    order = fields.IntegerField(required=True, unique=True)
    products = fields.ListField(fields.ReferenceField(Product))
    user_id = fields.IntegerField(required=True, unique=True)
    order_time = fields.DateTimeField()
    deletion_time = fields.DateTimeField()


@instance.register
class Payment(Document):
    order = fields.ReferenceField(Order)
    status = fields.BooleanField()
    deletion_time = fields.DateTimeField()


# vegeta = User(email='vegeta@over9000.com', friends=[goku])
# vegeta.commit() #add to db
# vegeta.dump() #serialization
