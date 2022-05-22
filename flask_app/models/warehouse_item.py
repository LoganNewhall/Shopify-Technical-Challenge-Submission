from flask_app.config.mysqlconnection import connectToMySQL

class Warehouse_Item:
    db = 'warehouse_inventory'
    def __init__(self, data):
        self.item_id = data['item_id']
        self.warehouse_id = data['warehouse_id']
        self.quantity = data['quantity']

    @classmethod
    def get_warehouse_items(cls, data):
        query = 'SELECT * FROM warehouse_items JOIN items ON items.id = warehouse_items.item_id WHERE warehouse_id = %(warehouse_id)s;'
        warehouse_items = connectToMySQL(cls.db).query_db(query, data)
        return warehouse_items

    @classmethod
    def add_inventory(cls, data):
        query = 'INSERT INTO warehouse_items (item_id, warehouse_id, quantity) VALUES (%(item_id)s, %(warehouse_id)s, %(quantity)s) ON DUPLICATE KEY UPDATE quantity = quantity + %(quantity)s;'
        inventory = connectToMySQL(cls.db).query_db(query, data)
        return inventory

    @classmethod
    def remove_inventory(cls, data):
        query = 'UPDATE warehouse_items SET quantity = quantity - %(quantity)s WHERE warehouse_id = %(warehouse_id)s AND item_id = %(item_id)s;'
        updated_inventory = connectToMySQL(cls.db).query_db(query, data)
        query = 'DELETE FROM warehouse_items WHERE warehouse_id = %(warehouse_id)s AND item_id = %(item_id)s AND quantity <= 0;'
        connectToMySQL(cls.db).query_db(query, data)
        return updated_inventory