from flask.ext.login import login_required

__author__ = 'fantom'
import json
from flask import Blueprint, request, jsonify, render_template, url_for, Response, flash, send_from_directory, redirect
from app import db, API_KEY, API_KEY_ERROR, client, APP_ROOT
from app import models
import pandas

mod_mobile_user = Blueprint('mobile', __name__)


# Date handler for Create and Update Date
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


@mod_mobile_user.route('/login', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/FBlogin', methods=['GET', 'POST'])
def fb_login():
    birthday = None
    gender = None
    profile_pic = None
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        print(str(req_json))
        username = req_json['email']
        if 'birthday' in req_json.keys():
            birthday = req_json['birthday']
        if 'gender' in req_json.keys():
            gender = req_json['gender']
        if 'picture' in req_json.keys():
            profile_pic = req_json['picture']['data']['url']
        name = req_json['name']
        fb_token = req_json['fb_token']
        fb_id = req_json['id']
        # mobile = req_json['mobile']
        user = db.session.query(models.User).filter_by(email=username).all()
        if len(user) > 0:
            return jsonify(response=user[0].id)
        else:
            # no matching email
            user = models.User(name=name, DOB=birthday, gender=gender, email=username, fb_token=fb_token, fb_id=fb_id,
                               profile_pic=profile_pic)
            db.session.add(user)
            db.session.flush()
            new_id = user.id
            db.session.commit()
            return jsonify(response=new_id)
    return API_KEY_ERROR

#
# @mod_mobile_user.route('/HomePage/JSON')
# def home_page():
#     if request.headers.get('Authorization') == API_KEY:
#         current = 0
#         out_put = "["
#         categories = db.session.query(models.SubCategory)
#         count = categories.count()
#         print count
#         for category in categories:
#             current += 1
#             if count == current:
#                 items = db.session.query(models.Items).filter_by(cat_id=category.id)
#                 out_put += jsonify(Category=[i.serialize for i in items[:4]]).get_data(as_text=True)
#             else:
#                 items = db.session.query(models.Items).filter_by(cat_id=category.id)
#                 out_put += jsonify(Category=[i.serialize for i in items[:4]]).get_data(as_text=True)
#                 out_put += ","
#             print(current)
#         out_put += "]"
#         return out_put
#         # return jsonify(Category=[i.serialize for i in categories])
#     return API_KEY_ERROR


#

@mod_mobile_user.route('/HomePage/JSON')
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
                out_put += jsonify(Catname=category.name, Items=[i.serialize for i in items[:4]]).get_data(
                    as_text=True)
            else:
                items = db.session.query(models.Items).filter_by(cat_id=category.id)
                out_put += jsonify(Catname=category.name, Items=[i.serialize for i in items[:4]]).get_data(
                    as_text=True)
                out_put += ","
            print(current)
        out_put += "]"
        return out_put
        # return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@mod_mobile_user.route('/GetSubCategoriesById/<int:cat_id>/JSON')
def get_sub_categories_by_id(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.SubCategory).filter_by(parentCat=cat_id)
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@mod_mobile_user.route('/GetCategoryById/<int:cat_id>/JSON')
def get_category_by_id(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        category = db.session.query(models.Category).filter_by(id=cat_id)
        return jsonify(Category=[i.serialize for i in category])
    return API_KEY_ERROR


# @mod_mobile_user.route('/makeOrder/<int:item_id>/<int:user_id>')
# def make_order_temp(item_id, user_id):
#     if request.headers.get('Authorization') == API_KEY:
#         item = db.session.query(models.Items).filter_by(id=item_id).one()
#         user = db.session.query(models.User).filter_by(id=user_id).one()
#         order = models.Orders(user=user, item=item, quantity=1)
#         db.session.add(order)
#         db.session.commit()
#         orders = db.session.query(models.Orders).all()
#         return jsonify(orders=[i.serialize for i in orders])
#     return API_KEY_ERROR


@mod_mobile_user.route('/GetShop/<int:shop_id>/JSON')
def get_shop(shop_id):
    if request.headers.get('Authorization') == API_KEY:
        shops = db.session.query(models.Shop).filter_by(id=shop_id)
        return jsonify(Shop=[i.serialize for i in shops])
    return API_KEY_ERROR


@mod_mobile_user.route('/GetShopItems/<int:shop_id>/JSON')
def get_shop_items_json(shop_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(shop_id=shop_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@mod_mobile_user.route('/GetItem/<int:item_id>/JSON')
def get_item_json(item_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(id=item_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@mod_mobile_user.route('/GetItemByCategory/<int:cat_id>/JSON')
def get_item_by_cat_json(cat_id):
    if request.headers.get('Authorization') == API_KEY:
        items = db.session.query(models.Items).filter_by(cat_id=cat_id)
        return jsonify(Items=[i.serialize for i in items])
    return API_KEY_ERROR


@mod_mobile_user.route('/newShopItem', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/editShopItem', methods=['GET', 'POST'])
# Task 2: Create route for editShopItem function here
def edit_shop_item():
    if request.headers.get('Authorization') == API_KEY:
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
    return API_KEY_ERROR


# @mod_mobile_user.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/signup', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/signupShop', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/loginShop', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/addToShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
def add_to_shop_cart(user_id, item_id):
    if request.headers.get('Authorization') == API_KEY:
        user = db.session.query(models.User).filter_by(id=user_id).one()
        item = db.session.query(models.Items).filter_by(id=item_id).one()
        db.session.merge(models.ShoppingCart(user=user, item=item))
        db.session.commit()
        return redirect(url_for('get_user_shop_cart', user_id=user_id))
    return API_KEY_ERROR


# ToDo
@mod_mobile_user.route('/removeFromShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/getUserShopCart/<int:user_id>/', methods=['GET', 'POST'])
def get_user_shop_cart(user_id):
    if request.headers.get('Authorization') == API_KEY:
        cart_items = db.session.query(models.ShoppingCart).filter_by(user_id=user_id).all()
        return jsonify(Cart=[i.serialize for i in cart_items])
    return API_KEY_ERROR


@mod_mobile_user.route('/registerDevice', methods=['GET', 'POST'])
def register_device():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        user_id = req_json['user_id']
        device_token = req_json['device_token']
        user = db.session.query(models.User).filter_by(id=user_id).one()
        user.device_token = device_token
        print(device_token)
        # client.send(device_token, "welcome To Bubble!!")
        db.session.add(user)
        db.session.commit()
        return jsonify(response=device_token)
    return API_KEY_ERROR


@mod_mobile_user.route('/registerShopDevice', methods=['GET', 'POST'])
def register_shop_device():
    if request.headers.get('Authorization') == API_KEY:
        req_json = request.get_json()
        shop_id = req_json['shop_id']
        device_token = req_json['device_token']
        shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
        shop.device_token = device_token
        print(device_token)
        # client.send(device_token, "welcome To Bubble!!")
        db.session.add(shop)
        db.session.commit()
        return jsonify(response=device_token)
    return API_KEY_ERROR


@mod_mobile_user.route('/sendPush', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/sendPushAll', methods=['GET', 'POST'])
def send_push_all():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == "POST":
            users = db.session.query(models.User).all()
            message = request.form['message']
            title = request.form['title']
            body = request.form['body']
            icon = request.form['icon']
            for user in users:
                if None is not user.device_token:
                    client.send(user.device_token, message,
                                notification={'title': title, 'body': body, 'icon': icon})
                    flash("Sent To" + user.name)
        else:
            return Response('''
        <form action="" method="post">
            <p><input type=text name=message>
            <p><input type=text name=title>
            <p><input type=text name=body>
            <p><input type=text name=icon>
            <p><input type=submit value=Send>
        </form>
        ''')
    return API_KEY_ERROR


@mod_mobile_user.route('/getOrdersByShopID', methods=['GET', 'POST'])
@login_required
# Task 3: Create route for deleteShopItem function here
def get_shop_orders():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            shop_id = req_json['shop_id']
            orders = db.session.query(models.Orders).join(models.Items).filter(models.Items.shop_id == shop_id)
            return jsonify(Orders=[i.serialize for i in orders])
    return API_KEY_ERROR


@mod_mobile_user.route("/export", methods=['GET'])
@login_required
def doexport():
    orders = db.session.query(models.Orders).all()
    data = [i.serialize for i in orders]
    print(data)
    json_data = json.dumps(data, default=date_handler)
    pandas.read_json(json_data).to_excel("output.xlsx")
    return send_from_directory(directory=APP_ROOT, filename="output.xlsx")


@mod_mobile_user.route('/editUser', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/editCategory', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/newCategory', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/newSubCategory', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/editSubCategory', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/makeOrder', methods=['GET', 'POST'])
def make_order():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            item_id = req_json['item_id']
            user_id = req_json['user_id']
            quantity = req_json['quantity']
            item = db.session.query(models.Items).filter_by(id=item_id).one()
            user = db.session.query(models.User).filter_by(id=user_id).one()
            shop = db.session.query(models.Shop).filter_by(id=item.shop_id).one()
            order = db.session.query(models.Orders).filter_by(user_id=user_id, item_id=item_id).first()
            if order is None:
                order = models.Orders(user=user, item=item, quantity=quantity)
                client.send(user.device_token, "Order: " + item.name, notification={'title': "Order Sent",
                                                                                    'body': shop.shop_name + " Received Your Order"
                                                                                                             " and waiting for mod_mobile_userroval"})
                client.send(shop.device_token, "Order: " + item.name, notification={'title': "Order: " + item.name,
                                                                                    'body': "please response to this "
                                                                                            "order for " + item.name})
            else:
                order.quantity = quantity
                print("OrderID: " + str(order.id) + ", ItemID:" + str(item.id) + ", UserID:" + str(user.id))
                client.send(user.device_token, "Order: " + item.name, notification={'title': "Order Sent",
                                                                                    'body': "Your Order have been sent to shop "
                                                                                            "waiting for mod_mobile_userroval"})
                client.send(shop.device_token, "Order: " + item.name, notification={'title': "Order: " + item.name,
                                                                                    'body': "please response to this "
                                                                                            "order for " + item.name})
                db.session.add(order)
                db.session.commit()
            db.session.add(order)
            db.session.commit()

            return jsonify(response=1)
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@mod_mobile_user.route('/getOrdersByUser', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/editOrdersByUser', methods=['GET', 'POST'])
def edit_orders_by_user():
    if request.headers.get('Authorization') == API_KEY:
        if request.method == 'POST':
            req_json = request.get_json()
            order_id = req_json['order_id']
            order = db.session.query(models.Orders).filter_by(id=order_id).one()
            if req_json['shipping_address'] is not None:
                order.shipping_address = req_json['shipping_address']
            db.session.add(order)
            db.session.commit()
            # return jsonify(orders=[i.serialize for i in orders])
            return jsonify(response=1)
        else:
            return jsonify(response=-1)
    return API_KEY_ERROR


@mod_mobile_user.route('/getUser', methods=['GET', 'POST'])
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


@mod_mobile_user.route('/editShop', methods=['GET', 'POST'])
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