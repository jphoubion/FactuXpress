# Generated by Django 4.2 on 2024-07-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoicing", "0009_company_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="type",
            field=models.CharField(
                choices=[
                    (None, "Sélectionnez..."),
                    ("srl", "SRL"),
                    ("sa", "SA"),
                    ("sc", "SC"),
                    ("snc", "SNC"),
                    ("scomm", "SComm"),
                    ("soc. simple", "Soc. Simple"),
                    ("autre", "Autre"),
                ],
                max_length=15,
            ),
        ),
    ]
