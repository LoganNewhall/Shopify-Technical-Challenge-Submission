from flask_app.config.mysqlconnection import connectToMySQL

class Warehouse:
    db = 'warehouse_inventory'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO warehouses (name, location) VALUES (%(name)s, %(location)s);'
        warehouse = connectToMySQL(cls.db).query_db(query, data)
        return warehouse

    @classmethod
    def get_warehouses(cls):
        query = 'SELECT * FROM warehouses;'
        warehouse_info = connectToMySQL(cls.db).query_db(query)
        return warehouse_info

    @classmethod
    def get_warehouse_by_id(cls, data):
        query = 'SELECT * FROM warehouses WHERE id = %(id)s'
        warehouse_id = connectToMySQL(cls.db).query_db(query, data)
        return warehouse_id[0]
        
    @classmethod
    def update_warehouse(cls, data):
        query = 'UPDATE warehouses SET name = %(name)s, location = %(location)s WHERE id = %(id)s'
        updated_warehouse = connectToMySQL(cls.db).query_db(query, data)
        return updated_warehouse

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM warehouse_items WHERE warehouse_id = %(id)s;'
        connectToMySQL(cls.db).query_db(query, data)
        query = 'DELETE FROM warehouses WHERE id = %(id)s;'
        deleted_warehouse = connectToMySQL(cls.db).query_db(query, data)
        return deleted_warehouse