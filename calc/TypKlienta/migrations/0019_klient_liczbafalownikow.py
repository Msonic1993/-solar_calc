# Generated by Django 3.1.4 on 2020-12-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0018_auto_20201215_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='LiczbaFalownikow',
            field=models.IntegerField(null=True),
        ),
    ]
