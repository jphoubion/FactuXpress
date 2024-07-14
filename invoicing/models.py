from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Company(models.Model):
    TYPES = (
        (None, 'Sélectionnez...'),
        ('srl','SRL'),
        ('sa','SA'),
        ('sc','SC'),
        ('snc','SNC'),
        ('scomm','SComm'),
        ('soc. simple','Soc. Simple'),
        ('autre','Autre'),
    )
    COUNTRIES = (
            (None, 'Sélectionnez...'),
            ('afghanistan', 'Afghanistan'),
            ('albania', 'Albania'),
            ('algeria', 'Algeria'),
            ('andorra', 'Andorra'),
            ('angola', 'Angola'),
            ('antigua and barbuda', 'Antigua and Barbuda'),
            ('argentina', 'Argentina'),
            ('armenia', 'Armenia'),
            ('australia', 'Australia'),
            ('austria', 'Austria'),
            ('azerbaijan', 'Azerbaijan'),
            ('bahamas', 'Bahamas'),
            ('bahrain', 'Bahrain'),
            ('bangladesh', 'Bangladesh'),
            ('barbados', 'Barbados'),
            ('belarus', 'Belarus'),
            ('belgium', 'Belgium'),
            ('belize', 'Belize'),
            ('benin', 'Benin'),
            ('bhutan', 'Bhutan'),
            ('bolivia', 'Bolivia'),
            ('bosnia and herzegovina', 'Bosnia and Herzegovina'),
            ('botswana', 'Botswana'),
            ('brazil', 'Brazil'),
            ('brunei', 'Brunei'),
            ('bulgaria', 'Bulgaria'),
            ('burkina faso', 'Burkina Faso'),
            ('burundi', 'Burundi'),
            ('cabo verde', 'Cabo Verde'),
            ('cambodia', 'Cambodia'),
            ('cameroon', 'Cameroon'),
            ('canada', 'Canada'),
            ('central african republic', 'Central African Republic'),
            ('chad', 'Chad'),
            ('chile', 'Chile'),
            ('china', 'China'),
            ('colombia', 'Colombia'),
            ('comoros', 'Comoros'),
            ('congo, democratic republic of the', 'Congo, Democratic Republic of the'),
            ('congo, republic of the', 'Congo, Republic of the'),
            ('costa rica', 'Costa Rica'),
            ('croatia', 'Croatia'),
            ('cuba', 'Cuba'),
            ('cyprus', 'Cyprus'),
            ('czech republic', 'Czech Republic'),
            ('denmark', 'Denmark'),
            ('djibouti', 'Djibouti'),
            ('dominica', 'Dominica'),
            ('dominican republic', 'Dominican Republic'),
            ('ecuador', 'Ecuador'),
            ('egypt', 'Egypt'),
            ('el salvador', 'El Salvador'),
            ('equatorial guinea', 'Equatorial Guinea'),
            ('eritrea', 'Eritrea'),
            ('estonia', 'Estonia'),
            ('eswatini', 'Eswatini'),
            ('ethiopia', 'Ethiopia'),
            ('fiji', 'Fiji'),
            ('finland', 'Finland'),
            ('france', 'France'),
            ('gabon', 'Gabon'),
            ('gambia', 'Gambia'),
            ('georgia', 'Georgia'),
            ('germany', 'Germany'),
            ('ghana', 'Ghana'),
            ('greece', 'Greece'),
            ('grenada', 'Grenada'),
            ('guatemala', 'Guatemala'),
            ('guinea', 'Guinea'),
            ('guinea-bissau', 'Guinea-Bissau'),
            ('guyana', 'Guyana'),
            ('haiti', 'Haiti'),
            ('honduras', 'Honduras'),
            ('hungary', 'Hungary'),
            ('iceland', 'Iceland'),
            ('india', 'India'),
            ('indonesia', 'Indonesia'),
            ('iran', 'Iran'),
            ('iraq', 'Iraq'),
            ('ireland', 'Ireland'),
            ('israel', 'Israel'),
            ('italy', 'Italy'),
            ('jamaica', 'Jamaica'),
            ('japan', 'Japan'),
            ('jordan', 'Jordan'),
            ('kazakhstan', 'Kazakhstan'),
            ('kenya', 'Kenya'),
            ('kiribati', 'Kiribati'),
            ('korea, north', 'Korea, North'),
            ('korea, south', 'Korea, South'),
            ('kosovo', 'Kosovo'),
            ('kuwait', 'Kuwait'),
            ('kyrgyzstan', 'Kyrgyzstan'),
            ('laos', 'Laos'),
            ('latvia', 'Latvia'),
            ('lebanon', 'Lebanon'),
            ('lesotho', 'Lesotho'),
            ('liberia', 'Liberia'),
            ('libya', 'Libya'),
            ('liechtenstein', 'Liechtenstein'),
            ('lithuania', 'Lithuania'),
            ('luxembourg', 'Luxembourg'),
            ('madagascar', 'Madagascar'),
            ('malawi', 'Malawi'),
            ('malaysia', 'Malaysia'),
            ('maldives', 'Maldives'),
            ('mali', 'Mali'),
            ('malta', 'Malta'),
            ('marshall islands', 'Marshall Islands'),
            ('mauritania', 'Mauritania'),
            ('mauritius', 'Mauritius'),
            ('mexico', 'Mexico'),
            ('micronesia', 'Micronesia'),
            ('moldova', 'Moldova'),
            ('monaco', 'Monaco'),
            ('mongolia', 'Mongolia'),
            ('montenegro', 'Montenegro'),
            ('morocco', 'Morocco'),
            ('mozambique', 'Mozambique'),
            ('myanmar', 'Myanmar'),
            ('namibia', 'Namibia'),
            ('nauru', 'Nauru'),
            ('nepal', 'Nepal'),
            ('netherlands', 'Netherlands'),
            ('new zealand', 'New Zealand'),
            ('nicaragua', 'Nicaragua'),
            ('niger', 'Niger'),
            ('nigeria', 'Nigeria'),
            ('north macedonia', 'North Macedonia'),
            ('norway', 'Norway'),
            ('oman', 'Oman'),
            ('pakistan', 'Pakistan'),
            ('palau', 'Palau'),
            ('panama', 'Panama'),
            ('papua new guinea', 'Papua New Guinea'),
            ('paraguay', 'Paraguay'),
            ('peru', 'Peru'),
            ('philippines', 'Philippines'),
            ('poland', 'Poland'),
            ('portugal', 'Portugal'),
            ('qatar', 'Qatar'),
            ('romania', 'Romania'),
            ('russia', 'Russia'),
            ('rwanda', 'Rwanda'),
            ('saint kitts and nevis', 'Saint Kitts and Nevis'),
            ('saint lucia', 'Saint Lucia'),
            ('saint vincent and the grenadines', 'Saint Vincent and the Grenadines'),
            ('samoa', 'Samoa'),
            ('san marino', 'San Marino'),
            ('sao tome and principe', 'Sao Tome and Principe'),
            ('saudi arabia', 'Saudi Arabia'),
            ('senegal', 'Senegal'),
            ('serbia', 'Serbia'),
            ('seychelles', 'Seychelles'),
            ('sierra leone', 'Sierra Leone'),
            ('singapore', 'Singapore'),
            ('slovakia', 'Slovakia'),
            ('slovenia', 'Slovenia'),
            ('solomon islands', 'Solomon Islands'),
            ('somalia', 'Somalia'),
            ('south africa', 'South Africa'),
            ('south sudan', 'South Sudan'),
            ('spain', 'Spain'),
            ('sri lanka', 'Sri Lanka'),
            ('sudan', 'Sudan'),
            ('suriname', 'Suriname'),
            ('sweden', 'Sweden'),
            ('switzerland', 'Switzerland'),
            ('syria', 'Syria'),
            ('taiwan', 'Taiwan'),
            ('tajikistan', 'Tajikistan'),
            ('tanzania', 'Tanzania'),
            ('thailand', 'Thailand'),
            ('timor-leste', 'Timor-Leste'),
            ('togo', 'Togo'),
            ('tonga', 'Tonga'),
            ('trinidad and tobago', 'Trinidad and Tobago'),
            ('tunisia', 'Tunisia'),
            ('turkey', 'Turkey'),
            ('turkmenistan', 'Turkmenistan'),
            ('tuvalu', 'Tuvalu'),
            ('uganda', 'Uganda'),
            ('ukraine', 'Ukraine'),
            ('united arab emirates', 'United Arab Emirates'),
            ('united kingdom', 'United Kingdom'),
            ('united states', 'United States'),
            ('uruguay', 'Uruguay'),
            ('uzbekistan', 'Uzbekistan'),
            ('vanuatu', 'Vanuatu'),
            ('vatican city', 'Vatican City'),
            ('venezuela', 'Venezuela'),
            ('vietnam', 'Vietnam'),
            ('yemen', 'Yemen'),
            ('zambia', 'Zambia'),
            ('zimbabwe', 'Zimbabwe'),
    )
    type = models.CharField(choices=TYPES,max_length=15,blank=False) # Company type : SCS, SRL,...
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    street = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    box = models.CharField(max_length=10, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(choices=COUNTRIES, max_length=40, blank=False, default='belgique')
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_dealer_or_customer = models.CharField(max_length=20,choices=(("dealer", "Dealer"), ("customer", "Customer")),
                                            blank=False,default='customer',help_text="Sélectionnez une ou plusieurs valeurs")

    def __str__(self) -> str:
        return f"{self.name} {self.type} - {self.city}"

class Customer(models.Model):
    lastname = models.CharField(max_length=30, unique=True, blank=False, null=False)
    firstname = models.CharField(max_length=30, unique=True, blank=False, null=False)
    street = models.CharField(max_length=100,blank=True,null=True)
    number = models.CharField(max_length=10,blank=True,null=True)
    box = models.CharField(max_length=10, blank=True, null=True)
    postcode = models.CharField(max_length=10,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(choices=Company.COUNTRIES, max_length=40, blank=False,default='belgique')
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.lastname} {self.firstname}"


class Item(models.Model):
    UNITY_OF_MESURE = (
        ('M', 'Mètre(s)'),
        ('KG', 'KG'),
        ('PC', 'Pièce(s)')
    )
    fastcode = models.CharField(max_length=10, blank=False, unique=True)
    description = models.TextField(max_length=255, blank=True)
    unity_of_mesure = models.CharField(max_length=10,choices=UNITY_OF_MESURE)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2,blank=False, null=0)
    remark = models.TextField(max_length=255)

    def __str__(self) -> str:
        return f"{self.fastcode} {self.description} : price = {self.unit_price}"

class Invoice(models.Model):
    pass


class Invoice_line(models.Model):
    pass
