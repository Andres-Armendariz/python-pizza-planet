from faker import Faker
from app.plugins import db
from app.repositories.models import Beverage


def generate_beverages(number_beverages):
    fake = Faker()
    fake_beverages = []
    for _ in range(number_beverages):
        beverage = Beverage(
            name=fake.word(),
            price=fake.random.randrange(1, 4),
        )
        fake_beverages.append(beverage)
    db.session.add_all(fake_beverages)
    db.session.commit()
