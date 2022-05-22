
from flask_app.config.mysqlconnection import connectToMySQL

class Item:
    db = 'warehouse_inventory'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO items (name, description) VALUES (%(name)s, %(description)s);'
        item = connectToMySQL(cls.db).query_db(query, data)
        return item

    @classmethod
    def get_items(cls):
        query = 'SELECT items.id, items.name, items.description, SUM(warehouse_items.quantity) quantity FROM items LEFT JOIN warehouse_items ON items.id = warehouse_items.item_id GROUP BY items.id;'
        item_info = connectToMySQL(cls.db).query_db(query)
        return item_info

    @classmethod
    def get_item_by_id(cls, data):
        query = 'SELECT * FROM items WHERE id = %(id)s'
        item_id = connectToMySQL(cls.db).query_db(query, data)
        return item_id[0]
    
    @classmethod
    def update_item(cls, data):
        query = 'UPDATE items SET name = %(name)s, description = %(description)s WHERE id = %(id)s'
        updated_item = connectToMySQL(cls.db).query_db(query, data)
        return updated_item

    @classmethod
    def delete_item(cls, data):
        query = 'DELETE FROM warehouse_items WHERE item_id = %(id)s;'
        connectToMySQL(cls.db).query_db(query, data)
        query = 'DELETE FROM items WHERE id = %(id)s;'
        deleted_item = connectToMySQL(cls.db).query_db(query, data)
        return deleted_item