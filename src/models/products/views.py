from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.products.products import Product
import src.models.products.errors as ProductErrors
import src.models.users.decorators as user_decorators

__author__ = 'Dartaku'


products_blueprint = Blueprint('products', __name__)


@products_blueprint.route('/manage/', methods=['GET'])
@user_decorators.requires_admin_permissions
def manage_products():
    return render_template("admin/products/manage_products.html")


@products_blueprint.route('/manage/add', methods=['GET', 'POST'])
@user_decorators.requires_admin_permissions
def add_products():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        size = request.form['size']
        price = request.form['price']
        ccy = request.form['ccy']
        sku_id = request.form['skuid']

        try:
            if Product.add_product(name, size, price, ccy, sku_id):
                return render_template("admin/add_products.html")
        except ProductErrors.SKUIDAlreadyRegisteredError as e:
            error = e.message
        except ProductErrors.ProductNameAlreadyRegisteredError as e:
            error = e.message

    return render_template("admin/products/add_products.html", error=error)