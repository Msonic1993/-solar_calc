# Generated by Django 3.1.3 on 2020-12-05 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0010_auto_20201205_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='WymaganaMoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TypKlienta.wymaganamocinstalacji'),
        ),
    ]
