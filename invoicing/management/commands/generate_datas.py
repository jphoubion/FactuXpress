from django.core.management.base import BaseCommand

import random
from faker import Faker
from ...models import User, Company, Customer, Item, Invoice, Invoice_line

class Command(BaseCommand):
    help = "Generates data in the DB"

    def handle(self, *args, **options) -> str | None:

        NOMS_SOCIETE = [
            "Google",
            "Apple",
            "Microsoft",
            "Amazon",
            "Facebook",
            "Tesla",
            "IBM",
            "Intel",
            "Oracle",
            "Samsung",
            "Sony",
            "Huawei",
            "Cisco",
            "HP",
            "Dell",
            "Nvidia",
            "AMD",
            "Salesforce",
            "Adobe",
            "Uber"
        ]
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

        fake = Faker()

        Company.objects.get_or_create(
            type=random.choice(Company.TYPES),
            name=random.choice(NOMS_SOCIETE),
            street=random.choice(NOMS_DES_RUES)
            )
