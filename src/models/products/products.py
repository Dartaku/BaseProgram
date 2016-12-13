import datetime
import uuid
from flask import session
from src.common.database import Database
from src.models.products.constants import *
import src.models.products.errors as ProductErrors

__author__ = 'Dartaku'


class Product(object):
    def __init__(self, name, size, price, currency, sku_id, created_date= datetime.datetime.utcnow(), updated_date = datetime.datetime.utcnow(),_id=None):
        self.name = name
        self.size = size
        self.price = price
        self.currency = currency
        self.sku_id = sku_id
        self.created_date = created_date
        self.updated_date = updated_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "name": self.name,
            "size": self.size,
            "price": self.price,
            "currency": self.currency,
            "sku_id": self.sku_id,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert(ProductCollection, self.json())

    @classmethod
    def retrieve_product_from_product_id(cls, product_id):
        product_data = Database.find_one(ProductCollection, query={'_id': product_id})
        return cls(**product_data)

    @staticmethod
    def add_product(name, size, price, ccy, sku_id):
        product_sku_id_data = Database.find_one(ProductCollection, {"sku_id": sku_id})
        product_name_data = Database.find_one(ProductCollection, {"name": name})
        if product_sku_id_data is not None:
            raise ProductErrors.SKUIDAlreadyRegisteredError("The SKU ID you have used already exists.")
        if product_name_data is not None:
            raise ProductErrors.ProductNameAlreadyRegisteredError("The Product name you have used already exists.")
        Product(name, size, price, ccy, sku_id).save_to_mongo()
        return True

# To Test
# Database.initialize()
# test = Product('test_product_name', 'product size', '10.00', 'SGD', 'SKU100001')
# test.save_to_mongo()