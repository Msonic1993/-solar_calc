# Generated by Django 3.1.4 on 2020-12-15 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0019_klient_liczbafalownikow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klient',
            old_name='WartoscFalownika',
            new_name='WartoscFalownikow',
        ),
    ]
