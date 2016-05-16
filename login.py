__author__ = 'fantom'
from app import app, db, API_KEY_ERROR, API_KEY
from flask import jsonify, request, Blueprint

import models

login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
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


@login.route('/FBlogin', methods=['GET', 'POST'])
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
