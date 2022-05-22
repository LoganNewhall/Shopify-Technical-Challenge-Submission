from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.warehouse import Warehouse
from flask_app.models.warehouse_item import Warehouse_Item

@app.route('/addwarehouse')
def add_warehouse():
    return render_template('add_warehouse.html')

@app.route('/new_warehouse', methods=['POST'])
def new_warehouse():
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
    }
    warehouse = Warehouse.save(data)
    return redirect('/')

@app.route('/delete/warehouse/<warehouse_id>')
def delete_warehouse(warehouse_id):
    data = {
        'id' : warehouse_id
    }
    delete_warehouse = Warehouse.delete(data)
    return redirect('/')

@app.route('/edit/warehouse/<warehouse_id>')
def edit_warehouse(warehouse_id):
    data = {
        'id' : warehouse_id
    }
    return render_template('warehouse.html', warehouse = Warehouse.get_warehouse_by_id(data))

@app.route('/update_warehouse/<warehouse_id>', methods=['POST'])
def update_warehouse(warehouse_id):
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'id' : warehouse_id
    }
    Warehouse.update_warehouse(data)
    return redirect('/')

@app.route('/view/<warehouse_id>')
def view(warehouse_id):
    data = {
        'id' : warehouse_id
    }
    warehouse_data = {
        'warehouse_id' : warehouse_id
    }
    return render_template('display_warehouse.html', warehouse = Warehouse.get_warehouse_by_id(data), warehouse_items = Warehouse_Item.get_warehouse_items(warehouse_data))