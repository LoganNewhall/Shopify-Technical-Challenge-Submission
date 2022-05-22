from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.warehouse_item import Warehouse_Item
from flask_app.models.item import Item
from flask_app.models.warehouse import Warehouse

@app.route('/add_inventory/<warehouse_id>')
def add_inventory(warehouse_id):
    data ={
        'id' : warehouse_id
    }
    return render_template('add_inventory.html', warehouse = Warehouse.get_warehouse_by_id(data), items = Item.get_items())

@app.route('/insert/<warehouse_id>', methods=['POST'])
def insert(warehouse_id):
    data = {
        'warehouse_id' : warehouse_id,
        'item_id' : request.form['item_id'],
        'quantity' : request.form['quantity']
    }
    Warehouse_Item.add_inventory(data)
    return redirect(f'/view/{warehouse_id}')

@app.route('/remove_inventory/<warehouse_id>/<item_id>', methods=['POST'])
def remove_inventory(warehouse_id, item_id):
    print(request.form)
    data ={
        'warehouse_id' : warehouse_id,
        'item_id' : item_id,
        'quantity' : request.form['remove']
    }
    Warehouse_Item.remove_inventory(data)
    return redirect(f'/view/{warehouse_id}')