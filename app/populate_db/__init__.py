from app.populate_db.beverage import generate_beverages
from app.populate_db.ingredient import generate_ingredients
from app.populate_db.size import generate_sizes
from app.populate_db.order import generate_orders


def generate_fake_data():
    generate_beverages(10)
    generate_ingredients(10)
    generate_sizes(5)
    return generate_orders(100)
