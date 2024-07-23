import django
from django.core.management.base import BaseCommand

import random
from faker import Faker
from ...models import User, Company, Customer, Item, Invoice, Invoice_line

class Command(BaseCommand):
    help = "Generates data in the DB"

    def handle(self, *args, **options) -> str | None:

        NOMS_DES_RUES = [
            "Rue de la République",
            "Avenue des Champs-Élysées",
            "Boulevard Saint-Germain",
            "Place de la Concorde",
            "Rue du Faubourg Saint-Honoré",
            "Avenue Montaigne",
            "Rue de Rivoli",
            "Boulevard Haussmann",
            "Rue Saint-Antoine",
            "Place Vendôme",
            "Rue de la Paix",
            "Avenue Victor Hugo",
            "Rue de Rennes",
            "Boulevard de Sébastopol",
            "Place de l'Étoile",
            "Rue de la Boétie",
            "Boulevard Malesherbes",
            "Rue de Tournon",
            "Avenue Kléber",
            "Boulevard Raspail"
        ]
        VILLES = [
            "New York",
            "London",
            "Tokyo",
            "Paris",
            "Sydney",
            "Beijing",
            "Moscow",
            "Dubai",
            "Singapore",
            "Los Angeles",
            "Mumbai",
            "Rio de Janeiro",
            "Istanbul",
            "Seoul",
            "Buenos Aires",
            "Cape Town",
            "Berlin",
            "Mexico City",
            "Bangkok",
            "Hong Kong",
            "Toronto",
            "Jakarta",
            "Cairo",
            "Rome",
            "Madrid",
            "Kuala Lumpur",
            "Chicago",
            "Lagos",
            "Sao Paulo",
            "Vienna"
        ]

        fake = Faker()
        print("Generation des COMPANY")
        types = [t[0] for t in Company.TYPES] # create a list from the tuple to get the left value
        countries = [c[0] for c in Company.COUNTRIES]
        for _ in range(20):
            Company.objects.get_or_create(
                type=random.choice(types[1:]), # slice to avoid value NONE
                name=fake.unique.company(),
                street=random.choice(NOMS_DES_RUES),
                number=random.choice(range(1,50)),
                box=random.choice(range(0,10)),
                postcode=random.choice(range(1000,9999)),
                city=random.choice(VILLES),
                country=random.choice(countries[1:]),
                phone=random.choice(range(1000000,9999999)),
                email=fake.unique.email(),
                is_dealer=random.choice([True, False]),
                is_customer=random.choice([True, False]),
                is_active=random.choice([True, False])
            )
            fake.unique.clear()

        print("Generation des CUSTOMER")
        for _ in range(20):
            Customer.objects.get_or_create(
                lastname=fake.unique.last_name(),
                firstname=fake.unique.first_name(),
                street=random.choice(NOMS_DES_RUES),
                number=random.choice(range(1,50)),
                box=random.choice(range(0,10)),
                postcode=random.choice(range(1000,9999)),
                city=random.choice(VILLES),
                country=random.choice(Company.COUNTRIES),
                phone=random.choice(range(1000000,9999999)),
                email=fake.unique.email(),
                company=random.choice(Company.objects.all())
                )
            fake.unique.clear()

        User.objects.create_superuser(username='naruto', password='belg1que')