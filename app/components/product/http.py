from sanic import Blueprint

from .views import (
    list_products,
)

products = Blueprint("products", url_prefix="/products")

products.add_route(list_products, "/", methods=["GET"])
