# Generated by Django 4.1.3 on 2022-11-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies_derevative", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="date",
            field=models.DateField(null=True),
        ),
    ]