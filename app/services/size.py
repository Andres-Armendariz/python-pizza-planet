from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request
from ..controllers import SizeController
from .base import entity_response


size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    size, error = SizeController.create(request.json)
    return entity_response(size, error)


@size.route('/', methods=PUT)
def update_size():
    size, error = SizeController.update(request.json)
    return entity_response(size, error)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    size, error = SizeController.get_by_id(_id)
    return entity_response(size, error)


@size.route('/', methods=GET)
def get_sizes():
    sizes, error = SizeController.get_all()
    return entity_response(sizes, error)
