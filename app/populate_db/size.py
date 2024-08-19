from faker import Faker
from app.plugins import db
from app.repositories.models import Size


def generate_sizes(number_sizes):
    fake = Faker()
    fake_sizes = []
    for _ in range(number_sizes):
        size = Size(
            name=fake.word(),
            price=fake.random.randrange(3, 8),
        )
        fake_sizes.append(size)
    db.session.add_all(fake_sizes)
    db.session.commit()
