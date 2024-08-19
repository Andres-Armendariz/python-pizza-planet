from faker import Faker


def generate_client_data():
    fake = Faker()
    return {
        "client_name": fake.name(),
        "client_dni": fake.random_int(min=1000000000, max=2499999999),
        "client_address": fake.address(),
        "client_phone": fake.phone_number(),
    }
