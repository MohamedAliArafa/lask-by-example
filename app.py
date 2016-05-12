import os
import json
from time import mktime
from flask_pushjack import FlaskGCM
from flask_restplus import Api, Resource, fields
from datetime import datetime
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, Response, send_from_directory
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from flask.ext.sqlalchemy import SQLAlchemy
import pandas

app = Flask(__name__)
# api = Api(app, version='1.0', title='Bubble API', description='bubble mobile app api API')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

config = {
    'GCM_API_KEY': 'AIzaSyCzQAHq4TuZV8J6YKZvQnyKrNSHyGp-b54'
}
app.config.update(config)

client = FlaskGCM()
client.init_app(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

API_KEY = '627562626c6520617069206b6579'
API_KEY_ERROR = "Invalid API KEY"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

import models


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    user = db.session.query(models.Shop).filter_by(id=user_id).first()
    print(user.is_authenticated)
    return user


@app.route("/loginTemp", methods=["GET", "POST"])
def login_temp():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.session.query(models.Shop).filter_by(owner_email=username, password=password).first()
        if user is None:
            flash('Username or Password is invalid', 'error')
            return Response('<p>Username or Password is invalid</p>')
        else:
            user.authenticated = True
            login_user(user)
            flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('get_shop_items', shop_id=user.id))
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout_temp():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    print(e)
    return redirect(url_for('login_temp'))


@app.route('/')
def welcome():
    # Welcome.
    return render_template('welcome.html')


@app.route('/summery')
@login_required
def summery():
    user = db.session.query(models.User).filter_by(id=1).first()
    print(user.is_authenticated)
    # Functions Documentation.
    return render_template('summery.html')


@app.route('/users')
def get_users():
    if request.headers.get('Authorization') == API_KEY:
        users = db.session.query(models.User).all()
        return jsonify(User=[i.serialize for i in users])
    return API_KEY_ERROR


# @app.route('/owners')
# def get_owners():
#     users = db.session.query(models.ShopOwner).all()
#     return jsonify(User=[i.serialize for i in users])


@app.route('/editUser', methods=['GET', 'POST'])
def edit_user():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            user_id = req_json['user_id']
            name = req_json['name']
            email = req_json['email']
            gender = req_json['gender']
            password = req_json['password']
            mobile = req_json['mobile']
            profile_pic = req_json['profile_pic']
            user = db.session.query(models.User).filter_by(id=user_id).one()
            if not (name is None):
                user.name = name
            if not (email is None):
                user.email = email
            if not (gender is None):
                user.gender = gender
            if not (password is None):
                user.password = password
            if not (mobile is None):
                user.mobile = mobile
            if not (profile_pic is None):
                user.profile_pic = profile_pic
            db.session.add(user)
            db.session.commit()
            # flash("New Item Added!!")
            return 1
        return API_KEY_ERROR


@app.route('/GetAllShops/JSON')
def get_all_shops():
    if request.headers.get('Authorization') == API_KEY:
        shops = db.session.query(models.Shop).all()
        return jsonify(Shop=[i.serialize for i in shops])
    return API_KEY_ERROR


@app.route('/GetCategories/JSON')
def get_all_categories():
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.Category).all()
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@app.route('/GetSubCategories/JSON')
def get_sub_categories():
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.SubCategory).all()
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@app.route('/HomePage/JSON')
def home_page():
    if request.headers.get('Authorization') == API_KEY:
        current = 0
        out_put = "["
        categories = db.session.query(models.SubCategory)
        count = categories.count()
        print count
        for category in categories:
            current += 1
            if count == current:
                items = db.session.query(models.Items).filter_by(cat_id=category.id)
                out_put += jsonify(Category=[i.serialize for i in items[:4]]).get_data(as_text=True)
            else:
                items = db.session.query(models.Items).filter_by(cat_id=category.id)
                out_put += jsonify(Category=[i.serialize for i in items[:4]]).get_data(as_text=True)
                out_put += ","
            print(current)
        out_put += "]"
        return out_put
        # return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@app.route('/HomePageTest/JSON')
def home_page_test():
    if request.headers.get('Authorization') == API_KEY:
        current = 0
        out_put = "["
        categories = db.session.query(models.SubCategory)
        count = categories.count()
        print count
        for category in categories:
            current += 1
            if count == current:
                items = db.session.query(models.Items).filter_by(cat_id=category.id)
                out_put += jsonify(Catname=category.name, Category=[i.serialize for i in items[:4]]).get_data(
                    as_text=True)
            else:
                items = db.session.query(models.Items).filter_by(cat_id=category.id)
                out_put += jsonify(Catname=category.name, Category=[i.serialize for i in items[:4]]).get_data(
                    as_text=True)
                out_put += ","
            print(current)
        out_put += "]"
        return out_put
        # return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@app.route('/editCategory', methods=['GET', 'POST'])
def edit_category():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            cat_id = req_json['cat_id']
            name = req_json['name']
            has_sub = req_json['hasSub']
            cat = db.session.query(models.Category).filter_by(id=cat_id).one()
            if not (name is None):
                cat.name = name
            if not (has_sub is None):
                cat.hasSub = has_sub
            db.session.add(cat)
            db.session.commit()
            # flash("New Item Added!!")
            return "Success"
    return API_KEY_ERROR


@app.route('/newCategory', methods=['GET', 'POST'])
def new_category():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            if request.form['name'] and request.form['hasSub']:
                new_cat = models.Category(name=request.form['name'], hasSub=request.form['hasSub'])
                db.session.add(new_cat)
                db.session.commit()
            # flash("New Item Added!!")
            return redirect(url_for('get_all_categories'))
        else:
            return render_template('newCategory.html')
    return API_KEY_ERROR


@app.route('/newSubCategory', methods=['GET', 'POST'])
def new_sub_category():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            cat_id = req_json['cat_id']
            name = req_json['name']
            cat = db.session.query(models.Category).filter_by(id=cat_id).one()
            if not (name is None):
                new_cat = models.SubCategory(name=name, category=cat)
                db.session.add(new_cat)
                db.session.commit()
            # flash("New Item Added!!")
            return 1
    return API_KEY_ERROR


@app.route('/editSubCategory', methods=['GET', 'POST'])
def edit_sub_category():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            cat_id = req_json['cat_id']
            name = req_json['name']
            parent_id = req_json['parent_id']
            cat = db.session.query(models.SubCategory).filter_by(id=cat_id).one()
            if not (name is None):
                cat.name = name
            if not (parent_id is None):
                cat.category = db.session.query(models.Category).filter_by(id=parent_id).one()
            db.session.add(cat)
            db.session.commit()
            # flash("New Item Added!!")
            return 1
    return API_KEY_ERROR


@app.route('/GetSubCategoriesById/<int:cat_id>/JSON')
def get_sub_categories_by_id(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.SubCategory).filter_by(parentCat=cat_id)
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@app.route('/GetCategoryById/<int:cat_id>/JSON')
def get_category_by_id(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        category = db.session.query(models.Category).filter_by(id=cat_id)
        return jsonify(Category=[i.serialize for i in category])
    return API_KEY_ERROR


@app.route('/Orders/JSON')
def get_orders():
    if request.headers.get('Authorization') == API_KEY:
        orders = db.session.query(models.Orders).all()
        return jsonify(orders=[i.serialize for i in orders])
    return API_KEY_ERROR


@app.route('/makeOrder/<int:item_id>/<int:user_id>')
def make_order_temp(item_id, user_id):
    if request.headers.get('Authorization') == API_KEY:
        item = db.session.query(models.Items).filter_by(id=item_id).one()
        user = db.session.query(models.User).filter_by(id=user_id).one()
        order = models.Orders(user=user, item=item, quantity=1)
        db.session.add(order)
        db.session.commit()
        orders = db.session.query(models.Orders).all()
        return jsonify(orders=[i.serialize for i in orders])
    return API_KEY_ERROR


@app.route('/makeOrder', methods=['GET', 'POST'])
def make_order():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            item_id = req_json['item_id']
            user_id = req_json['user_id']
            quantity = req_json['quantity']
            item = db.session.query(models.Items).filter_by(id=item_id).one()
            user = db.session.query(models.User).filter_by(id=user_id).one()
            order = db.session.query(models.Orders).filter_by(user_id=user_id, item_id=item_id).first()
            if order is None:
                order = models.Orders(user=user, item=item, quantity=quantity)
            else:
                order.quantity = quantity
                print(order.id)
                db.session.add(order)
                db.session.commit()
            db.session.add(order)
            db.session.commit()

            return jsonify(response=1)
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/getOrdersByUser', methods=['GET', 'POST'])
def get_orders_by_user():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            user_id = req_json['user_id']
            orders = db.session.query(models.Orders).filter_by(user_id=user_id)
            return jsonify(orders=[i.serialize for i in orders])
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/getUser', methods=['GET', 'POST'])
def get_user():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            user_id = req_json['user_id']
            user = db.session.query(models.User).filter_by(id=user_id)
            return jsonify(orders=[i.serialize for i in user])
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/editShop', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def edit_shop():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            shop_id = req_json['shop_id']
            owner_name = req_json['owner_name']
            owner_email = req_json['owner_email']
            gender = req_json['gender']
            owner_date_of_birth = req_json['owner_date_of_birth']
            owner_profile_pic = req_json['owner_profile_pic']
            shop_name = req_json['shop_name']
            shop_profile_pic = req_json['shop_profile_pic']
            shop_cover_pic = req_json['shop_cover_pic']
            mobile = req_json['mobile']
            # short_description = req_json['short_description']
            description = req_json['description']
            longitude = req_json['longitude']
            latitude = req_json['latitude']
            shop_address = req_json['shop_address']
            shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
            if not (owner_name is None):
                shop.owner_name = owner_name
            if not (owner_email is None):
                shop.owner_email = owner_email
            if not (gender is None):
                shop.gender = gender
            if not (owner_date_of_birth is None):
                shop.owner_date_of_birth = owner_date_of_birth
            if not (owner_profile_pic is None):
                shop.owner_profile_pic = owner_profile_pic
            if not (shop_name is None):
                shop.shop_name = shop_name
            if not (shop_profile_pic is None):
                shop.shop_profile_pic = shop_profile_pic
            if not (shop_cover_pic is None):
                shop.shop_cover_pic = shop_cover_pic
            if not (mobile is None):
                shop.mobile = mobile
            # if not (short_description is None):
            #     shop.short_description = short_description
            if not (description is None):
                shop.description = description
            if not (longitude is None):
                shop.longitude = longitude
            if not (latitude is None):
                shop.latitude = latitude
            if not (shop_address is None):
                shop.shop_address = shop_address
            db.session.add(shop)
            db.session.commit()
            # flash("New Item Added!!")
            return jsonify(response=1)
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/GetShop/<int:shop_id>/JSON')
def get_shop(shop_id):
    if request.headers.get('Authorization') == API_KEY:
        shops = db.session.query(models.Shop).filter_by(id=shop_id)
        return jsonify(Shop=[i.serialize for i in shops])
    return API_KEY_ERROR


@app.route('/GetShopItems/<int:shop_id>/JSON')
def get_shop_items_json(shop_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(shop_id=shop_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@app.route('/GetItem/<int:item_id>/JSON')
def get_item_json(item_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(id=item_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@app.route('/GetItemByCategory/<int:cat_id>/JSON')
def get_item_by_cat_json(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(cat_id=cat_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@app.route('/GetShopItems')
def get_shop_items():
    print("current_user: " + str(current_user.id))
    shop_id = request.args.get('shop_id')
    print("shop_id: " + str(shop_id))
    if int(current_user.id) == int(shop_id):
        shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
        items = db.session.query(models.Items).filter_by(shop_id=shop_id)
        return render_template('menu.html', shop=shop, items=items)
    else:
        return Response('Not Authorized')


@app.route('/newShopItem', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def new_shop_item():
    req_json = request.get_json()
    shop_id = req_json['shop_id']
    name = req_json['name']
    quantity = req_json['quantity']
    price = req_json['price']
    description = req_json['description']
    # short_description = req_json['short_description']
    image = req_json['image']
    cat_id = req_json['cat_id']
    global new_item
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    if request.method == 'POST':
        category = db.session.query(models.SubCategory).filter_by(id=cat_id).one()
        new_item = models.Items(name=name, quantity=quantity, shop=shop, SubCategory=category,
                                # short_description=short_description,
                                price=price, description=description, image=image)
        try:
            db.session.add(new_item)
            db.session.flush()
            new_id = new_item.id
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return jsonify(response=new_id)
    else:
        return jsonify(response=-1)


@app.route('/editShopItem', methods=['GET', 'POST'])
# Task 2: Create route for editShopItem function here
def edit_shop_item():
    req_json = request.get_json()
    shop_id = req_json['shop_id']
    item_id = req_json['item_id']
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    categories = db.session.query(models.SubCategory).all()
    item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        if not (req_json['name'] is None):
            item.name = req_json['name']
        if not (req_json['description'] is None):
            item.description = req_json['description']
        # if not (req_json['short_description'] is None):
        #     item.description = req_json['short_description']
        if not (req_json['quantity'] is None):
            item.quantity = req_json['quantity']
        if not (req_json['price'] is None):
            item.price = req_json['price']
        if not (req_json['cat_id'] is None):
            item.category = db.session.query(models.SubCategory).filter_by(id=req_json['cat_id']).one()
            item.cat_id = req_json['cat_id']
        if not (req_json['image'] is None):
            # filename = secure_filename(image_file.filename)
            item.image = req_json['image']
        db.session.add(item)
        db.session.commit()
        # flash("New Item Edited!!")
        return jsonify(response=1)
    else:
        return render_template('editMenuItem.html', shop=shop, item=item, categories=categories)


# @app.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
# # Task 3: Create route for deleteShopItem function here
# def delete_shop_item(shop_id, item_id):
#     shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
#     item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
#     if request.method == 'POST':
#         db.session.delete(item)
#         db.session.commit()
#         # flash("New Item DELETED!!")
#         return redirect(url_for('get_shop_items_json', shop_id=shop_id))
#     else:
#         return render_template('deleteMenuItem.html', shop=shop, item=item)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        username = req_json['email']
        password = req_json['password']
        user = db.session.query(models.User).filter_by(email=username).all()
        if len(user) > 0:
            if user[0].password == password:
                return jsonify(response=user)
            else:
                # wrong password
                return jsonify(response=-1)
        else:
            # no matching email
            return jsonify(response=-2)
    return API_KEY_ERROR


@app.route('/FBlogin', methods=['GET', 'POST'])
def fb_login():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        print(str(req_json))
        username = req_json['email']
        birthday = req_json['birthday']
        gender = req_json['gender']
        name = req_json['name']
        fb_token = req_json['fb_token']
        # mobile = req_json['mobile']
        user = db.session.query(models.User).filter_by(email=username).all()
        if len(user) > 0:
            return jsonify(response=user[0].id)
        else:
            # no matching email
            user = models.User(name= name, DOB=birthday, gender=gender, email=username, fb_token=fb_token)
            db.session.add(user)
            db.session.flush()
            new_id = user.id
            db.session.commit()
            return jsonify(response=new_id)
    return API_KEY_ERROR


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        username = req_json['email']
        password = req_json['password']
        mobile = req_json['mobile']
        if db.session.query(models.User).filter_by(email=username):
            user = db.session.query(models.User).filter_by(email=username).all()
            if len(user) > 0:
                if user[0].email == username:
                    # email already exist
                    return jsonify(response=-2)
                if user[0].mobile == mobile:
                    # mobile already exist
                    return jsonify(response=-3)
            else:
                user = models.User(email=username, password=password, mobile=mobile)
                try:
                    db.session.add(user)
                    db.session.flush()
                    new_id = user.id
                    db.session.commit()
                    # user_added = db.session.query(models.User).filter_by(email=username).all()
                    return jsonify(response=new_id)
                except:
                    db.session.rollback()
                    raise
        else:
            # error
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/signupShop', methods=['GET', 'POST'])
def signup_shop():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        # shop_name = req_json['shop_name']
        # shop_profile_pic = req_json['shop_profile_pic']
        # shop_cover_pic = req_json['shop_cover_pic']
        mobile = req_json['mobile']
        # short_description = req_json['short_description']
        # description = req_json['description']
        # longitude = req_json['longitude']
        # latitude = req_json['latitude']
        # shop_address = req_json['shop_address']
        owner_name = req_json['owner_name']
        owner_email = req_json['owner_email']
        password = req_json['password']
        if db.session.query(models.Shop).filter_by(owner_email=owner_email):
            shop = db.session.query(models.Shop).filter_by(owner_email=owner_email).all()
            if len(shop) > 0:
                if shop[0].owner_email == owner_email:
                    # name already exist
                    return jsonify(response=shop[0].id)
            else:
                shop = models.Shop(owner_name=owner_name, owner_email=owner_email, password=password, mobile=mobile)
                try:
                    db.session.add(shop)
                    db.session.flush()
                    new_id = shop.id
                    db.session.commit()
                except:
                    db.session.rollback()
                    raise
                return jsonify(response=new_id)
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@app.route('/loginShop', methods=['GET', 'POST'])
def login_shop():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        username = req_json['email']
        password = req_json['password']
        user = db.session.query(models.Shop).filter_by(owner_email=username).all()
        if len(user) > 0:
            if user[0].password == password:
                return jsonify(response=user[0].id)
            else:
                # wrong password
                return jsonify(response=-1)
        else:
            # no matching email
            return jsonify(response=-2)
    return API_KEY_ERROR


@app.route('/addToShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
def add_to_shop_cart(user_id, item_id):
    if request.headers.get('Authorization') == API_KEY:
        user = db.session.query(models.User).filter_by(id=user_id).one()
        item = db.session.query(models.Items).filter_by(id=item_id).one()
        db.session.merge(models.ShoppingCart(user=user, item=item))
        db.session.commit()
        return redirect(url_for('get_user_shop_cart', user_id=user_id))
    return API_KEY_ERROR


@app.route('/removeFromShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
def remove_from_shop_cart(user_id, item_id):
    if request.headers.get('Authorization') == API_KEY:
        user = db.session.query(models.User).filter_by(id=user_id).one()
        item = db.session.query(models.Items).filter_by(id=item_id).one()
        if db.session.query(models.ShoppingCart).filter_by(user=user, item=item):
            db.session.query(models.ShoppingCart).filter_by(user=user, item=item).one()
            db.session.delete(item)
            db.session.commit()
            return redirect(url_for('get_user_shop_cart', user_id=user_id))
        return redirect(url_for('get_user_shop_cart', user_id=user_id))
    return API_KEY_ERROR


@app.route('/getUserShopCart/<int:user_id>/', methods=['GET', 'POST'])
def get_user_shop_cart(user_id):
    if request.headers.get('Authorization') == API_KEY:
        cart_items = db.session.query(models.ShoppingCart).filter_by(user_id=user_id).all()
        return jsonify(Cart=[i.serialize for i in cart_items])
    return API_KEY_ERROR


@app.route('/registerDevice', methods=['GET', 'POST'])
def register_device():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        user_id = req_json['user_id']
        device_token = req_json['device_token']
        user = db.session.query(models.User).filter_by(id=user_id).one()
        user.device_token = device_token
        print(device_token)
        client.send(device_token, "welcome To Bubble!!")
        db.session.add(user)
        db.session.commit()
        return jsonify(response=device_token)
    return API_KEY_ERROR


@app.route('/sendPush', methods=['GET', 'POST'])
def send_push():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == "POST":
            if request.form['user_id']:
                user_id = request.form['user_id']
                message = request.form['message']
                user = db.session.query(models.User).filter_by(id=user_id).one()
                client.send(user.device_token, message)
                return Response('<p>SENT to: ' + user.device_token)
            else:
                return
        else:
            return Response('''
        <form action="" method="post">
            <p><input type=text name=user_id>
            <p><input type=text name=message>
            <p><input type=submit value=Send>
        </form>
        ''')
    return API_KEY_ERROR


@app.route('/signUpShopTemp', methods=['GET', 'POST'])
@login_required
def sign_up_shop_temp():
    if request.method == 'POST':
        if request.form['name'] and request.form['owner']:
            new_shop = models.Shop(shop_name=request.form['name'], shop_profile_pic=request.form['profile_pic'],
                                   owner_name=request.form['owner'], owner_email=request.form['email'],
                                   password=request.form['password'], mobile=request.form['mobile'],
                                   description=request.form['description'], shop_address=request.form['shop_address'])
            db.session.add(new_shop)
            login_user(new_shop)
            db.session.flush()
            new_id = new_shop.id
            db.session.commit()
            flash("Shop Added!!")
            return redirect(url_for('new_shop_item_temp', shop_id=new_id))
    return render_template('newShop.html')  # @app.route('/')


@app.route('/newShopItem/<int:shop_id>/', methods=['GET', 'POST'])
@login_required
# Task 1: Create route for newShopItem function here
def new_shop_item_temp(shop_id):
    global new_item
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['quantity']:
            new_item = models.Items(name=request.form['name'], quantity=request.form['quantity'], shop=shop,
                                    cat_id=request.form.get('cat_id'), price=request.form['price'],
                                    description=request.form['description'], image=request.form['profile_pic'])
            db.session.add(new_item)
            db.session.commit()
            flash("New Item Added!!")
        return redirect(url_for('get_shop_items', shop_id=shop_id))
    else:
        return render_template('newMenuItem.html', shop=shop)


@app.route('/editShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
@login_required
# Task 2: Create route for editShopItem function here
def edit_shop_item_temp(shop_id, item_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['quantity']:
            item.quantity = request.form['quantity']
        if request.form['price']:
            item.price = request.form['price']
        if request.form.get('cat_id'):
            print('category', request.form.get('cat_id'))
            item.cat_id = request.form['cat_id']
        if request.form['image']:
            image_file = request.form['image']
            item.image = image_file

        item.images = [{"id": 1, "url": "570269c0f2302.png"}, {"id": 2, "url": "570269c0f2302.png"},
                       {"id": 3, "url": "570269c0f2302.png"}, {"id": 4, "url": "570269c0f2302.png"},
                       {"id": 5, "url": "570269c0f2302.png"}, ]
        db.session.add(item)
        db.session.commit()
        flash("New Item Edited!!")
        return redirect(url_for('get_shop_items', shop_id=shop_id))
    else:
        return render_template('editMenuItem.html', shop=shop, item=item)


@app.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
@login_required
# Task 3: Create route for deleteShopItem function here
def delete_shop_item_temp(shop_id, item_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        flash("New Item DELETED!!")
        return redirect(url_for('get_shop_items', shop_id=shop_id))
    else:
        return render_template('deleteMenuItem.html', shop=shop, item=item)


@app.route("/export", methods=['GET'])
@login_required
def doexport():
    orders = db.session.query(models.Orders).all()
    data = [i.serialize for i in orders]
    print(data)
    json_data = json.dumps(data, default=date_handler)
    pandas.read_json(json_data).to_excel("output.xlsx")
    return send_from_directory(directory=APP_ROOT, filename="output.xlsx")


# def hello():
#     print(os.environ['APP_SETTINGS'])
#     return "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
