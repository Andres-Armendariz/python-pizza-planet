from faker import Faker
from app.plugins import db
from app.repositories.models import Ingredient


def generate_ingredients(number_ingredients):
    fake = Faker()
    fake_ingredients = []
    for _ in range(number_ingredients):
        ingredient = Ingredient(
            name=fake.word(),
            price=fake.random.randrange(1, 4),
        )
        fake_ingredients.append(ingredient)
    db.session.add_all(fake_ingredients)
    db.session.commit()
