# Generated by Django 3.1.3 on 2020-12-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0030_auto_20201222_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='KosztWiFiExtender',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='KosztZwyszka',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='WiFiExtender',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='Zwyszka',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
