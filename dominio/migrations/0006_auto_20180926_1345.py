# Generated by Django 2.1.1 on 2018-09-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0005_auto_20180925_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formaingresso',
            options={'ordering': ['nome'], 'verbose_name': 'Forma de ingresso', 'verbose_name_plural': 'Formas de ingresso'},
        ),
    ]