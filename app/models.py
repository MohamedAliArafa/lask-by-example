from app import db
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION


class Images(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'url': self.url,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class AgentsRole(db.Model):
    __tablename__ = 'agents_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Agents(db.Model):
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    passwd = db.Column(db.String)
    active = db.Column(db.Boolean)
    role_id = db.Column(db.Integer, db.ForeignKey('agents_role.id'))
    role = db.relationship(AgentsRole)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def is_active(self):
        return self.active

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.firstname,
            'last_name': self.lastname,
            'email': self.email,
            'active': self.active,
            'role_id': self.role_id,
            'role_name': self.role.name,
            'date_add': self.created,
            'date_upd': self.updated
        }


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwd = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.CHAR)
    fav_lan = db.Column(db.Integer)
    longitude = db.Column(DOUBLE_PRECISION)
    latitude = db.Column(DOUBLE_PRECISION)
    google_id = db.Column(db.String)
    fb_token = db.Column(db.String)
    fb_id = db.Column(db.String)
    device_token = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def is_active(self):
        return self.active

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'birthday': self.birthday,
            'gender': self.gender,
            'fav_lan': self.fav_lan,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'fb_token': self.fb_token,
            'google_id': self.google_id,
            'device_token': self.device_token,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users)
    floor_num = db.Column(db.Integer)
    building_num = db.Column(db.Integer)
    street_name = db.Column(db.String)
    description = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'floor_num': self.floor_num,
            'building_num': self.building_num,
            'street_name': self.street_name,
            'description': self.description,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Phone(db.Model):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users)
    code = db.Column(db.Integer)
    number = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'code': self.floor_num,
            'number': self.building_num,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class UserImages(db.Model):
    __tablename__ = 'user_images'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users)
    id_image = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship(Images)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_image': self.floor_num,
            'image_url': self.image.url,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class OrderStatus(db.Model):
    __tablename__ = 'order_status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    id_current_state = db.Column(db.Integer, db.ForeignKey('order_status.id'))
    status = db.relationship(OrderStatus)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users)
    id_address = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship(Address)
    id_phone = db.Column(db.Integer, db.ForeignKey('phone.id'))
    phone = db.relationship(Phone)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_image': self.floor_num,
            'image_url': self.image.url,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class OrderProcess(db.Model):
    __tablename__ = 'order_process'

    id = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship(OrderStatus)
    id_agent = db.Column(db.Integer, db.ForeignKey('agents.id'))
    agent = db.relationship(Agents)
    id_status = db.Column(db.Integer, db.ForeignKey('order_status.id'))
    status = db.relationship(OrderStatus)
    message = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_image': self.floor_num,
            'image_url': self.image.url,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    id_parent = db.Column(db.Integer)
    level_depth = db.Column(db.Integer)
    name = db.Column(db.String(20), nullable=False)
    id_image = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship(Images)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_parent': self.id_parent,
            'level_depth': self.level_depth,
            'name': self.name,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500))
    id_supplier = db.Column(db.Integer)
    id_manufacturer = db.Column(db.Integer)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String(8))
    on_sale = db.Column(db.Boolean)
    wholesale_price = db.Column(db.DECIMAL)
    reduction_price = db.Column(db.DECIMAL)
    reduction_percent = db.Column(db.FLOAT)
    reduction_from = db.Column(db.DateTime)
    reduction_to = db.Column(db.DateTime)
    out_of_stock = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'id_supplier': self.id_supplier,
            'id_manufacturer': self.id_manufacturer,
            'id_category': self.id_category,
            'category': self.category.name,
            'quantity': self.quantity,
            'price': self.price,
            'on_sale': self.on_sale,
            'wholesale_price': self.wholesale_price,
            'reduction_price': self.reduction_price,
            'reduction_percent': self.reduction_percent,
            'reduction_from': self.reduction_from,
            'reduction_to': self.reduction_to,
            'out_of_stock': self.out_of_stock,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class ProductAttribute(db.Model):
    __tablename__ = 'product_attribute'

    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship(Products)
    attr_name = db.Column(db.String)
    attr_description = db.Column(db.String)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_product': self.id_product,
            'product': self.product.name,
            'attr_name': self.attr_name,
            'attr_description': self.attr_description,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class ProductImages(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship(Products)
    id_image = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship(Images)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_product': self.id_product,
            'product': self.product.name,
            'id_image': self.id_image,
            'image_url': self.image.url,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class UserRecentlyViewed(db.Model):
    __tablename__ = 'use_recently_viewed'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(Users)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship(Products)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_product': self.floor_num,
            'product': self.product.name,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }


class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship(Orders)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship(Products)
    quantity = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    date_add = db.Column(db.DateTime, server_default=db.func.now())
    date_upd = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'id_order': self.id_order,
            'id_product': self.id_product,
            'active': self.active,
            'date_add': self.date_add,
            'date_upd': self.date_upd
        }
