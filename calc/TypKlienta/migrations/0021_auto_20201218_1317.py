# Generated by Django 3.1.4 on 2020-12-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0020_auto_20201215_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='LiczbaOptymalizatorow',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='NazwaOptymalizatora',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='WartoscOptymalizatorow',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
    ]
