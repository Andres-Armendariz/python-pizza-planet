from app.common.http_methods import GET, POST
from flask import Blueprint, request
from ..controllers import OrderController
from .base import entity_response


order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    order, error = OrderController.create(request.json)
    return entity_response(order, error)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    order, error = OrderController.get_by_id(_id)
    return entity_response(order, error)


@order.route('/', methods=GET)
def get_orders():
    orders, error = OrderController.get_all()
    return entity_response(orders, error)
