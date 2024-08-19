from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request
from ..controllers import IngredientController
from .base import entity_response


ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    ingredient, error = IngredientController.create(request.json)
    return entity_response(ingredient, error)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    ingredient, error = IngredientController.update(request.json)
    return entity_response(ingredient, error)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    ingredient, error = IngredientController.get_by_id(_id)
    return entity_response(ingredient, error)


@ingredient.route('/', methods=GET)
def get_ingredients():
    ingredients, error = IngredientController.get_all()
    return entity_response(ingredients, error)
