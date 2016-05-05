from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String)
    owner_email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    gender = db.Column(db.CHAR)
    shop_name = db.Column(db.String(250))
    shop_profile_pic = db.Column(db.String(200))
    shop_cover_pic = db.Column(db.String(200))
    mobile = db.Column(db.String)
    description = db.Column(db.String(250))
    short_description = db.Column(db.String(250))
    longitude = db.Column(db.String)
    latitude = db.Column(db.String)
    shop_address = db.Column(db.String(150))
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.shop_name,
            'profile_pic': self.shop_profile_pic,
            'cover_pic': self.shop_cover_pic,
            'mobile': self.mobile,
            'owner_email': self.owner_email,
            'shop_address': self.shop_address,
            'short_description': self.short_description,
            'description': self.description,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'owner_name': self.owner_name,
            'owner_profile_pic': self.shop_profile_pic,
            'created': self.created,
            'updated': self.updated
        }


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    hasSub = db.Column(db.String(5))

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'hasSub': self.hasSub
        }


class SubCategory(db.Model):
    __tablename__ = 'sub_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    parentCat = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category, foreign_keys=[parentCat])

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.name,
            'parentCat': self.category.id
        }


class Items(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    short_description = db.Column(db.String(250))
    description = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(50))
    images = db.Column(JSON)
    price = db.Column(db.String(8))
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))
    shop = db.relationship(Shop)
    cat_id = db.Column(db.Integer, db.ForeignKey('sub_category.id'))
    SubCategory = db.relationship(SubCategory)
    is_main = db.Column(db.Boolean)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'short_description': self.short_description,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'images': self.images,
            'shop_id': self.shop.id,
            'shop_name': self.shop.shop_name,
            'shop_short_desc': self.shop.short_description,
            'shop_image': self.shop.shop_profile_pic,
            'shop_address': self.shop.shop_address,
            'cat_id': self.SubCategory.category.id,
            'sub_cat_id': self.SubCategory.id,
            'is_main': self.is_main,
            'created': self.created,
            'updated': self.updated
        }


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    gender = db.Column(db.CHAR)
    DOB = db.Column(db.Date)
    profile_pic = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'gender': self.gender,
            'DOB': self.DOB,
            'password': self.password,
            'mobile': self.mobile,
            'profile_pic': self.profile_pic,
            'authenticated': self.authenticated,
            'created': self.created,
            'updated': self.updated
        }


class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'

    user = db.relationship(User)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    item = db.relationship(Items)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'shop_id': self.item.shop.id,
            'shop_name': self.item.shop.shop_name,
            'item_id': self.item.id,
            'item_name': self.item.name,
            'item_desc': self.item.description,
            'item_price': self.item.price,
            'created': self.created,
            'updated': self.updated
        }


class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship(User)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item = db.relationship(Items)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer)
    shipping_address = db.Column(db.String)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'shop_id': self.item.shop.id,
            'shop_name': self.item.shop.shop_name,
            'shop_address': self.item.shop.shop_address,
            'item_id': self.item.id,
            'item_name': self.item.name,
            'item_desc': self.item.description,
            'item_price': self.item.price,
            'item_quantity': self.quantity,
            'shipping_address': self.shipping_address,
            'created': self.created,
            'updated': self.updated
        }
