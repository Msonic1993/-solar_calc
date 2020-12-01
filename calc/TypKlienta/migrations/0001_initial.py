# Generated by Django 3.1.3 on 2020-11-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EkspozycjaDachowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ekspozycja', models.CharField(max_length=100)),
                ('mnoznik', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
            options={
                'verbose_name': 'Ekspozycja dachowa',
                'verbose_name_plural': 'Ekspozycja dachowa',
            },
        ),
        migrations.CreateModel(
            name='KadNachyleniaDachu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kadnachylenia', models.CharField(max_length=100)),
                ('przelicznik', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
            options={
                'verbose_name': 'Kąt nachylenia dachu',
                'verbose_name_plural': 'Kąt nachylenia dachu',
            },
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('wartosc', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
            options={
                'verbose_name': 'Vat',
                'verbose_name_plural': 'Vat',
            },
        ),
        migrations.CreateModel(
            name='TypKlienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True, max_length=300)),
                ('Vat', models.ManyToManyField(null=True, to='TypKlienta.Vat')),
            ],
            options={
                'verbose_name': 'Typ klienta',
                'verbose_name_plural': 'Typ klienta',
            },
        ),
    ]
