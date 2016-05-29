__author__ = 'fantom'
from flask import Blueprint, request, jsonify, render_template
from app import db, API_KEY, API_KEY_ERROR
from app import models

mod_admin = Blueprint('admin', __name__)


@mod_admin.route('/')
def summery():
    if request.headers.get('Authorization') == API_KEY:
        user = db.session.query(models.User).filter_by(id=1).first()
        print(user.is_authenticated)
        # Functions Documentation.
        return render_template('summery.html')
    return API_KEY_ERROR


@mod_admin.route('/users')
def get_users():
    if request.headers.get('Authorization') == API_KEY:
        users = db.session.query(models.User).all()
        return jsonify(User=[i.serialize for i in users])
    return API_KEY_ERROR


@mod_admin.route('/GetAllShops/JSON')
def get_all_shops():
    if request.headers.get('Authorization') == API_KEY:
        shops = db.session.query(models.Shop).all()
        return jsonify(Shop=[i.serialize for i in shops])
    return API_KEY_ERROR


@mod_admin.route('/GetCategories/JSON')
def get_all_categories():
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.Category).all()
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@mod_admin.route('/GetSubCategories/JSON')
def get_sub_categories():
    if request.headers.get('Authorization') == API_KEY:
        categories = db.session.query(models.SubCategory).all()
        return jsonify(Category=[i.serialize for i in categories])
    return API_KEY_ERROR


@mod_admin.route('/Orders/JSON')
def get_orders():
    if request.headers.get('Authorization') == API_KEY:
        orders = db.session.query(models.Orders).all()
        return jsonify(orders=[i.serialize for i in orders])
    return API_KEY_ERROR


@mod_admin.route('/editOrderByID/<int:order_id>/', methods=['GET', 'POST'])
def edit_order_by_id(order_id):
    if request.headers.get('Authorization') == API_KEY:
        order = db.session.query(models.Orders).filter_by(id=order_id).one()
        shop = order.item.shop
        if request.method == 'POST':
            if request.form['shipping_address'] is not None:
                order.shipping_address = request.form['shipping_address']
            if request.form['quantity'] is not None:
                order.quantity = request.form['quantity']
            db.session.add(order)
            db.session.commit()
            return render_template('Admin/OrdersList.html', shop=shop)
        else:
            return render_template('Admin/EditOrder.html', orders=order)
    return API_KEY_ERROR
