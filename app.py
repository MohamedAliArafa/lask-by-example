import os
import models
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def welcome():
    # Welcome.
    return render_template('welcome.html')


@app.route('/summery')
def summery():
    # Functions Documentation.
    return render_template('summery.html')


@app.route('/users')
def get_users():
    users = db.session.query(models.User).all()
    return jsonify(User=[i.serialize for i in users])


# @app.route('/owners')
# def get_owners():
#     users = db.session.query(models.ShopOwner).all()
#     return jsonify(User=[i.serialize for i in users])


@app.route('/editUser', methods=['GET', 'POST'])
def edit_user():
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


@app.route('/GetAllShops/JSON')
def get_all_shops():
    shops = db.session.query(models.Shop).all()
    return jsonify(Shop=[i.serialize for i in shops])


@app.route('/GetCategories/JSON')
def get_all_categories():
    categories = db.session.query(models.Category).all()
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/GetSubCategories/JSON')
def get_sub_categories():
    categories = db.session.query(models.SubCategory).all()
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/HomePage/JSON')
def home_page():
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


@app.route('/editCategory', methods=['GET', 'POST'])
def edit_category():
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


@app.route('/newCategory', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        if request.form['name'] and request.form['hasSub']:
            new_cat = models.Category(name=request.form['name'], hasSub=request.form['hasSub'])
            db.session.add(new_cat)
            db.session.commit()
        # flash("New Item Added!!")
        return redirect(url_for('get_all_categories'))
    else:
        return render_template('newCategory.html')


@app.route('/newSubCategory', methods=['GET', 'POST'])
def new_sub_category():
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


@app.route('/editSubCategory', methods=['GET', 'POST'])
def edit_sub_category():
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


@app.route('/GetSubCategoriesById/<int:cat_id>/JSON')
def get_sub_categories_by_id(cat_id):
    categories = db.session.query(models.SubCategory).filter_by(parentCat=cat_id)
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/GetCategoryById/<int:cat_id>/JSON')
def get_category_by_id(cat_id):
    category = db.session.query(models.Category).filter_by(id=cat_id)
    return jsonify(Category=[i.serialize for i in category])


@app.route('/editShop', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def edit_shop():
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


@app.route('/GetShop/<int:shop_id>/JSON')
def get_shop(shop_id):
    shops = db.session.query(models.Shop).filter_by(id=shop_id)
    return jsonify(Shop=[i.serialize for i in shops])


@app.route('/GetShopItems/<int:shop_id>/JSON')
def get_shop_items_json(shop_id):
    items = db.session.query(models.Items).filter_by(shop_id=shop_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetItem/<int:item_id>/JSON')
def get_item_json(item_id):
    items = db.session.query(models.Items).filter_by(id=item_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetItemByCategory/<int:cat_id>/JSON')
def get_item_by_cat_json(cat_id):
    items = db.session.query(models.Items).filter_by(cat_id=cat_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetShopItems/<int:shop_id>/')
def get_shop_items(shop_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    items = db.session.query(models.Items).filter_by(shop_id=shop_id)
    return render_template('menu.html', shop=shop, items=items)


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


@app.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
# Task 3: Create route for deleteShopItem function here
def delete_shop_item(shop_id, item_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        # flash("New Item DELETED!!")
        return redirect(url_for('get_shop_items_json', shop_id=shop_id))
    else:
        return render_template('deleteMenuItem.html', shop=shop, item=item)


@app.route('/login', methods=['GET', 'POST'])
def login():
    req_json = request.get_json()
    username = req_json['email']
    password = req_json['password']
    user = db.session.query(models.User).filter_by(email=username).all()
    if len(user) > 0:
        if user[0].password == password:
            return jsonify(response=user[0].id)
        else:
            # wrong password
            return jsonify(response=-1)
    else:
        # no matching email
        return jsonify(response=-2)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
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


@app.route('/signupShop', methods=['GET', 'POST'])
def signup_shop():
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


@app.route('/loginShop', methods=['GET', 'POST'])
def login_shop():
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


@app.route('/addToShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
def add_to_shop_cart(user_id, item_id):
    user = db.session.query(models.User).filter_by(id=user_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id).one()
    db.session.merge(models.ShoppingCart(user=user, item=item))
    db.session.commit()
    return redirect(url_for('get_user_shop_cart', user_id=user_id))


@app.route('/removeFromShopCart/<int:user_id>/<int:item_id>', methods=['GET', 'POST'])
def remove_from_shop_cart(user_id, item_id):
    user = db.session.query(models.User).filter_by(id=user_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id).one()
    if db.session.query(models.ShoppingCart).filter_by(user=user, item=item):
        db.session.query(models.ShoppingCart).filter_by(user=user, item=item).one()
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('get_user_shop_cart', user_id=user_id))
    return redirect(url_for('get_user_shop_cart', user_id=user_id))


@app.route('/getUserShopCart/<int:user_id>/', methods=['GET', 'POST'])
def get_user_shop_cart(user_id):
    cart_items = db.session.query(models.ShoppingCart).filter_by(user_id=user_id).all()
    return jsonify(Cart=[i.serialize for i in cart_items])


@app.route('/signUpShopTemp', methods=['GET', 'POST'])
def sign_up_shop_temp():
    if request.method == 'POST':
        if request.form['name'] and request.form['owner']:
            new_shop = models.Shop(shop_name=request.form['name'], shop_profile_pic=request.form['profile_pic'],
                                   owner_name=request.form['owner'], owner_email=request.form['email'],
                                   password=request.form['password'], mobile=request.form['mobile'],
                                   description=request.form['description'], shop_address=request.form['shop_address'])
            db.session.add(new_shop)
            db.session.flush()
            new_id = new_shop.id
            db.session.commit()
            flash("Shop Added!!")
            return redirect(url_for('new_shop_item_temp', shop_id=new_id))
    return render_template('newShop.html')  # @app.route('/')


@app.route('/newShopItem/<int:shop_id>/', methods=['GET', 'POST'])
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
        if request.files['image'] and allowed_file(request.files['image'].filename):
            image_file = request.files['image']
            item.image = image_file
        db.session.add(item)
        db.session.commit()
        flash("New Item Edited!!")
        return redirect(url_for('get_shop_items', shop_id=shop_id))
    else:
        return render_template('editMenuItem.html', shop=shop, item=item)


@app.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
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
def doexport():
    return excel.make_response_from_tables(db.session, [models.Shop, models.Items], "xls")
# def hello():
#     print(os.environ['APP_SETTINGS'])
#     return "Hello World!"
# 
# 
# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
