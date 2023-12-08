#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    return make_response([bakery.to_dict() for bakery in Bakery.query.all()], 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = db.session.get(Bakery, id)
    print(bakery)
    return make_response(jsonify(bakery.to_dict()), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    goods = BakedGood.query.all()
    sorted_goods = sorted(goods,key = lambda good: 1/good.price)
    return make_response([good.to_dict() for good in sorted_goods],200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():

    goods = BakedGood.query.all()
    priciest = sorted(goods,key = lambda good: 1/good.price)[0]
    return make_response(priciest.to_dict(),200)

    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
