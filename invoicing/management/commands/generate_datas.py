import django
from django.core.management.base import BaseCommand

import random
from faker import Faker
from ...models import User, Company, Customer, Item, Unity_of_measure, Invoice, Invoice_line

class Command(BaseCommand):
    help = "Generates data in the DB"
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

    types = [t[0] for t in Company.TYPES]  # create a list from the tuple to get the left value
    countries = [c[0] for c in Company.COUNTRIES]

    def handle(self, *args, **options) -> str | None:
        self.generate_companies()
        self.generate_customers()
        self.generate_unity()
        self.generate_items()
        self.generate_invoices()

    def generate_companies(self):
        print("Generation des COMPANY")

        for _ in range(20):
            Company.objects.get_or_create(
                type=random.choice(self.types[1:]), # slice to avoid value NONE
                name=self.fake.unique.company(),
                street=random.choice(self.NOMS_DES_RUES),
                number=random.choice(range(1,50)),
                box=random.choice(range(0,10)),
                postcode=random.choice(range(1000,9999)),
                city=random.choice(self.VILLES),
                country=random.choice(self.countries[1:]),
                phone=random.choice(range(1000000,9999999)),
                email=self.fake.unique.email(),
                is_dealer=random.choice([True, False]),
                is_customer=random.choice([True, False]),
                is_active=random.choice([True, False])
            )
            self.fake.unique.clear()

    def generate_customers(self):
        print("Generation des CUSTOMER")
        for _ in range(20):
            Customer.objects.get_or_create(
                lastname=self.fake.unique.last_name(),
                firstname=self.fake.unique.first_name(),
                street=random.choice(self.NOMS_DES_RUES),
                number=random.choice(range(1,50)),
                box=random.choice(range(0,10)),
                postcode=random.choice(range(1000,9999)),
                city=random.choice(self.VILLES),
                country=random.choice(self.countries[1:]),
                phone=random.choice(range(1000000,9999999)),
                email=self.fake.unique.email(),
                company=random.choice(Company.objects.all() or None)
                )
            self.fake.unique.clear()

    def generate_invoices(self):
        print("Generation des INVOICE")
        STATUS = [
            'quotation',
            'order',
            'invoice'
        ]
        for status in STATUS:
            for i in range(20):
                Invoice.objects.get_or_create(
                    customer=random.choice(Customer.objects.all()),
                    creation_date_time=self.fake.date_time_between(),
                    reference=f"{status[:3].upper()}/{random.choice(['2023', '2024'])}/{i}",
                    status=status
                )
                self.fake.unique.clear()

    def generate_unity(self):
        print("Generation des UNITY_OF_MEASURE")
        UNITY = [
            ('pc','Pièce(s)'),
            ('m','Mètre(s)'),
            ('box','Boite(s)')
        ]

        for unity in UNITY:
            for i in range(20):
                choice = random.choice(UNITY)
                Unity_of_measure.objects.get_or_create(
                    short_description=choice[0],
                    long_description=choice[1]
                )
                self.fake.unique.clear()

    def generate_items(self):
        print("Generation des ITEM")
        ITEMS = [
            ('FORINSTCOMP', 'Forfait installation complète',
             random.choice(Unity_of_measure.objects.all()), '120.00', "Remarque Forfait installation complète", False, False, None),
            ('FORINSTBAS', 'Forfait installation basique',
             random.choice(Unity_of_measure.objects.all()), '80.00', "Remarque forfait installation basique", False, False, None),
            ('FORBKP', 'Forfait sauvegarde complète',
             random.choice(Unity_of_measure.objects.all()), '60.00', 'Remarque Forfait sauvegarde', False, False, None),
            ('FORINSTLOG', 'Forfait installation logiciel',
             random.choice(Unity_of_measure.objects.all()), '100.00', 'remarque Forfait installation logiciel', False, False, None),
        ]

        # create a group item to ensure it's already in the DB
        unity_of_mesure = Unity_of_measure.objects.get(short_description="pc")
        Item.objects.get_or_create(
            fastcode="BUNDLEHPOFF71200", description="Bundle HP Officejet 71200", unity_of_measure=unity_of_mesure,
            unit_price="256.00", remark="Remarque Bundle HP Officejet 71200", is_a_group_item=True, is_a_child_item=False,
            parent_of_child_item=None
        )
        group_item = Item.objects.get(fastcode="BUNDLEHPOFF71200")

        Item.objects.get_or_create(
            fastcode="HPOFF71200", description="HP Officejet 71200", unity_of_measure=unity_of_mesure,
            unit_price="120.00", remark="Remarque HP Officejet 71200", is_a_group_item=False, is_a_child_item=True,
            parent_of_child_item=group_item
        )
        Item.objects.get_or_create(
            fastcode="USB3M", description="Câble USB 3 mètres", unity_of_measure=unity_of_mesure,
            unit_price="8.00", remark="Remarque Câble USB 3 mètres", is_a_group_item=False, is_a_child_item=True,
            parent_of_child_item=group_item
        )
        Item.objects.get_or_create(
            fastcode="HPOFF71200CART", description="Cartouches HP Officejet 71200 XL", unity_of_measure=unity_of_mesure,
            unit_price="128.00", remark="Remarque Cartouches HP Officejet 71200 XL", is_a_group_item=False, is_a_child_item=True,
            parent_of_child_item=group_item
        )

        for i in range(20):
            choice = random.choice(ITEMS)
            Item.objects.get_or_create(
                fastcode=choice[0],
                description=choice[1],
                unity_of_measure=choice[2],
                unit_price=choice[3],
                remark=choice[4],
                is_a_group_item=choice[5],
                is_a_child_item=choice[6],
                parent_of_child_item=choice[7]
            )
            self.fake.unique.clear()

        User.objects.create_superuser(username='naruto', password='belg1que')
