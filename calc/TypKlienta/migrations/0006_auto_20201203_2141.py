# Generated by Django 3.1.3 on 2020-12-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TypKlienta', '0005_auto_20201130_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='WymaganaMocInstalacji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdKlienta', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('WymaganaMoc', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='klient',
            name='metraz',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='klient',
            name='zuzycie',
            field=models.IntegerField(null=True),
        ),
    ]
