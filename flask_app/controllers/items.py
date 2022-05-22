from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.item import Item
from flask_app.models.warehouse import Warehouse

@app.route('/')
def index():
    return render_template('index.html', items = Item.get_items(), warehouses = Warehouse.get_warehouses())

@app.route('/additem')
def add_item():
    return render_template('add_item.html')

@app.route('/new_item', methods=['POST'])
def new_item():
    data = {
        'name' : request.form['name'],
        'description' : request.form['description']
    }
    item = Item.save(data)
    return redirect('/')

@app.route('/delete/item/<item_id>')
def delete_item(item_id):
    data = {
        'id' : item_id
    }
    delete_item = Item.delete_item(data)
    return redirect('/')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/edit/item/<item_id>')
def edit_item(item_id):
    data = {
        'id' : item_id
    }
    return render_template('item.html', item = Item.get_item_by_id(data))

@app.route('/update_item/<item_id>', methods=['POST'])
def update_item(item_id):
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'id' : item_id
    }
    Item.update_item(data)
    return redirect('/')