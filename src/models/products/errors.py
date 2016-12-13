__author__ = 'jslvtr'


class ProductErrors(Exception):
    def __init__(self, message):
        self.message = message


class SKUIDAlreadyRegisteredError(ProductErrors):
    pass


class ProductNameAlreadyRegisteredError(ProductErrors):
    pass


