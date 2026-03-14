from faker import Faker

fake = Faker("pt-BR")
print(fake.free_email())