# Generated by Django 3.1.3 on 2020-12-07 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0011_auto_20201205_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='WymaganaMoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TypKlienta.wymaganamocinstalacji'),
        ),
    ]
