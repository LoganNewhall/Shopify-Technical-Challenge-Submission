from flask_app import app
from flask_app.controllers import items, warehouse_items, warehouses
if __name__ == '__main__':
    app.run(debug=True)