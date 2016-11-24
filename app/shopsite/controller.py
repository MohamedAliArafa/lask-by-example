import json
import os
import mechanize
from flask import Blueprint, request, render_template, flash, redirect, url_for, Response
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import db, login_manager, models
from flask.ext.api.decorators import set_renderers
from flask.ext.api.renderers import HTMLRenderer
from HTMLParser import HTMLParser
from werkzeug.utils import secure_filename

__author__ = 'fantom'

mod_site = Blueprint('website', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class MLStripper(HTMLParser):
    def error(self, message):
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@login_manager.user_loader
def load_user(agent_id):
    print(agent_id)
    agent = db.session.query(models.Agents).filter_by(id=agent_id).first()
    print(agent.is_authenticated)
    return agent


# somewhere to logout
@mod_site.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('website.welcome'))


@mod_site.route('/')
@set_renderers(HTMLRenderer)
def welcome():
    # Welcome.
    if current_user.is_authenticated:
        return redirect(url_for('website.get_shop_items', shop_id=int(current_user.id)))
    else:
        return render_template('gentelella/production/login.html')


@mod_site.route('/signUpAgent', methods=['GET', 'POST'])
# @login_required
# route for GetShopItems function here
@set_renderers(HTMLRenderer)
def sign_up_agent():
    if request.method == 'POST':
        print("inside post")
        if request.form['first_name'] and request.form['last_name']:
            new_agent = models.Agents(first_name=request.form['first_name'], last_name=request.form['last_name'],
                                      email=request.form['email'], passwd=request.form['passwd'])
            db.session.add(new_agent)
            new_agent.authenticated = True
            login_user(new_agent)
            db.session.flush()
            new_id = new_agent.id
            db.session.commit()
            print("Agent " + new_agent.first_name)
            return redirect(url_for('website.home', agent_id=new_id))
    return render_template('gentelella/production/login.html')


@mod_site.route('/home')
# route for GetShopItems function here
@set_renderers(HTMLRenderer)
def home():
    print("current_user: " + str(current_user.id))
    agent_id = request.args.get('agent_id')
    print("shop_id: " + str(agent_id))
    if int(current_user.id) == int(agent_id):
        shop = db.session.query(models.Agents).filter_by(id=agent_id).one()
        return render_template('gentelella/production/index.html', agent=shop)
    else:
        return Response('Not Authorized')


@mod_site.route('/GetItems')
# route for GetShopItems function here
@set_renderers(HTMLRenderer)
def get_items():
    print("current_user: " + str(current_user.id))
    agent_id = request.args.get('agent_id')
    print("shop_id: " + str(agent_id))
    if int(current_user.id) == int(agent_id):
        agent = db.session.query(models.Agents).filter_by(id=agent_id).one()
        items = db.session.query(models.Products).all()
        return render_template('shop/ItemsList.html', agent=agent, items=items)
    else:
        return Response('Not Authorized')


@mod_site.route('/editMyShop/<int:agent_id>', methods=['GET', 'POST'])
# route for editMyShop function here
@set_renderers(HTMLRenderer)
def edit_agent(agent_id):
    if int(current_user.id) == int(agent_id):
        shop = db.session.query(models.Shop).filter_by(id=agent_id).one()
        if request.method == 'POST':
            if request.form['owner_name']:
                shop.owner_name = request.form['owner_name']
            if request.form['owner_email']:
                shop.owner_email = request.form['owner_email']
            if request.form['shop_name']:
                shop.shop_name = request.form['shop_name']
            if request.form['description']:
                shop.description = request.form['description']
            if request.form['shop_address']:
                shop.shop_address = request.form['shop_address']
            if request.form.get('mobile'):
                shop.mobile = request.form['mobile']
            if request.form['lon']:
                longitude = request.form['lon']
                shop.longitude = longitude
            if request.form['lat']:
                latitude = request.form['lat']
                shop.latitude = latitude
            db.session.add(shop)
            db.session.commit()
            flash("shop Edited!!")
            return redirect(url_for('website.get_shop_items', shop_id=agent_id))
        else:
            return render_template('shop/EditShop.html', shop=shop)
    else:
        Response("Not Authorised")


@mod_site.route('/editMyShop/uploadImage/<int:shop_id>', methods=['GET', 'POST'])
# route for editMyShop function here
@set_renderers(HTMLRenderer)
def edit_shop_image(shop_id):
    if int(current_user.id) == int(shop_id):
        shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
        if request.method == 'POST':
            if request.files['file']:
                # check if the post request has the file part
                if 'file' not in request.files:
                    flash('No file part')
                file_upload = request.files['file']
                # if user does not select file, browser also
                # submit a empty part without filename
                if file_upload.filename == '':
                    flash('No selected file')
                if file_upload and allowed_file(file_upload.filename):
                    filename = secure_filename(file_upload.filename)
                    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    browser = mechanize.Browser()
                    browser.open("http://bubble.zeowls.com/upload.php")
                    # file uploading
                    form = browser.form = browser.forms().next()
                    form.add_file(file_upload, filename=os.path.basename(filename))
                    send_response = browser.submit()
                    data = strip_tags(send_response.get_data().replace("\n", "").replace(" ", ""))
                    obj = json.loads(data)
                    image_file = obj['image']
                    shop.shop_profile_pic = image_file
            db.session.add(shop)
            db.session.commit()
            flash("shop Edited!!")
            return redirect(url_for('website.edit_shop', shop_id=shop_id))
        else:
            return render_template('shop/ImageUpload.html', shop=shop)
    else:
        Response("Not Authorised")


@mod_site.route('/uploadItemImage/<int:agent_id>/<int:item_id>', methods=['GET', 'POST'])
# route for editMyShop function here
@set_renderers(HTMLRenderer)
def edit_item_image(agent_id, item_id):
    if int(current_user.id) == int(agent_id):
        agent = db.session.query(models.Agents).filter_by(id=agent_id).one()
        item = db.session.query(models.Products).filter_by(id=item_id).one()
        if request.method == 'POST':
            if request.files['file']:
                # check if the post request has the file part
                if 'file' not in request.files:
                    flash('No file part')
                file_upload = request.files['file']
                # if user does not select file, browser also
                # submit a empty part without filename
                if file_upload.filename == '':
                    flash('No selected file')
                if file_upload and allowed_file(file_upload.filename):
                    filename = secure_filename(file_upload.filename)
                    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    browser = mechanize.Browser()
                    browser.open("http://bubble.zeowls.com/upload.php")
                    # file uploading
                    form = browser.form = browser.forms().next()
                    form.add_file(file_upload, filename=os.path.basename(filename))
                    send_response = browser.submit()
                    data = strip_tags(send_response.get_data().replace("\n", "").replace(" ", ""))
                    obj = json.loads(data)
                    image_file = obj['image']
                    item.main_image = image_file
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('website.get_items', agent_id=agent_id))
        else:
            return render_template('shop/ImageUpload.html', shop=item, agent=agent)
    else:
        Response("Not Authorised")


@mod_site.route('/newItem', methods=['GET', 'POST'])
@login_required
# route for newShopItem function here
@set_renderers(HTMLRenderer)
def new_item():
    agent_id = request.args.get('agent_id')
    if int(current_user.id) == int(agent_id):
        agent = db.session.query(models.Agents).filter_by(id=agent_id).one()
        main_cats = db.session.query(models.Category).all()
        if request.method == 'POST':
            if request.form['name'] and request.form['quantity']:
                newitem = models.Products(name=request.form['name'], quantity=request.form['quantity'],
                                          id_category=request.form.get('cat_id'), price=request.form['price'],
                                          description=request.form['description'])
                db.session.add(newitem)
                db.session.flush()
                new_id = newitem.id
                db.session.commit()
                print("item added id:" + str(new_id))
                return redirect(url_for('website.edit_item_image', agent_id=agent_id, item_id=new_id))
        else:
            return render_template('shop/new_item.html', agent=agent, main_cats=main_cats)
    else:
        return Response("Not Authorised")


@mod_site.route('/editShopItem/<int:agent_id>/<int:item_id>/', methods=['GET', 'POST'])
@login_required
# route for editShopItem function here
@set_renderers(HTMLRenderer)
def edit_shop_item(agent_id, item_id):
    if int(current_user.id) == int(agent_id):
        agent = db.session.query(models.Agents).filter_by(id=agent_id).one()
        item = db.session.query(models.Products).filter_by(id=item_id).one()
        main_cats = db.session.query(models.Category).all()
        # sub_cat = {}
        # for cat in main_cats:
        #     print(cat.name)
        #     sub_cat[cat.id] = db.session.query(models.SubCategory).filter_by(parentCat=cat.id)
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
            # item.images = [{"id": 1, "url": "570269c0f2302.png"}, {"id": 2, "url": "570269c0f2302.png"},
            #                {"id": 3, "url": "570269c0f2302.png"}, {"id": 4, "url": "570269c0f2302.png"},
            #                {"id": 5, "url": "570269c0f2302.png"}, ]
            db.session.add(item)
            db.session.commit()
            flash("New Item Edited!!")
            return redirect(url_for('website.ge_items', agent_id=agent_id))
        else:
            return render_template('shop/EditItem.html', agent=agent, item=item, main_cats=main_cats)
    else:
        return Response("Not Authorised")


@mod_site.route('/editItem/<int:item_id>/', methods=['GET', 'POST'])
@login_required
# route for editShopItem function here
@set_renderers(HTMLRenderer)
def edit_item(item_id):
    # if int(current_user.id) == int(shop_id):
    #     shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    item = db.session.query(models.Products).filter_by(id=item_id).one()
    main_cats = db.session.query(models.Category).all()
    # sub_cat = {}
    # for cat in main_cats:
    #     print(cat.name)
    #     sub_cat[cat.id] = db.session.query(models.SubCategory).filter_by(parentCat=cat.id)
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
        # item.images = [{"id": 1, "url": "570269c0f2302.png"}, {"id": 2, "url": "570269c0f2302.png"},
        #                {"id": 3, "url": "570269c0f2302.png"}, {"id": 4, "url": "570269c0f2302.png"},
        #                {"id": 5, "url": "570269c0f2302.png"}, ]
        db.session.add(item)
        db.session.commit()
        flash("New Item Edited!!")
        # return redirect(url_for('mobile.get_item_json'))
    else:
        return render_template('shop/EditItem.html', item=item, main_cats=main_cats)
        # else:
        #     return Response("Not Authorised")


@mod_site.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
@login_required
# route for deleteShopItem function here
@set_renderers(HTMLRenderer)
def delete_shop_item(shop_id, item_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    item = db.session.query(models.Items).filter_by(id=item_id, shop_id=shop_id).one()
    if int(current_user.id) == int(shop_id):
        if request.method == 'POST':
            db.session.delete(item)
            db.session.commit()
            flash("New Item DELETED!!")
            return redirect(url_for('website.get_shop_items', shop_id=shop_id))
        else:
            return render_template('shop/DeleteItem.html', shop=shop, item=item)
    return Response("Not Authorised")


@mod_site.route('/myOrders/<int:shop_id>', methods=['GET', 'POST'])
@login_required
# route for myOrders function here
@set_renderers(HTMLRenderer)
def get_shop_orders(shop_id):
    shop = db.session.query(models.Shop).filter_by(id=shop_id).one()
    if int(current_user.id) == int(shop_id):
        orders = db.session.query(models.Orders).join(models.Items).filter(models.Items.shop_id == shop_id)
        return render_template('shop/OrdersList.html', shop=shop, orders=orders)
    return Response("Not Authorised")


@mod_site.route("/login", methods=["GET", "POST"])
@set_renderers(HTMLRenderer)
def login():
    if request.method == 'POST':
        print("POST")
        errors = []
        username = request.form.get('username')
        password = request.form.get('password')
        print(username + ":" + password)
        agent = db.session.query(models.Agents).filter_by(email=username, passwd=password).first()
        if agent is None:
            # flash('Username or Password is invalid', 'error')
            errors.append("Username or Password is invalid")
            return render_template('gentelella/production/login.html', errors=errors)
        else:
            agent.authenticated = True
            login_user(agent)
            # flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('website.home', agent_id=agent.id))
    else:
        return render_template('gentelella/production/login.html')
