# Generated by Django 2.1.1 on 2018-09-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo_seletivo', '0003_auto_20180925_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processoseletivo',
            name='periodo_letivo',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2')], verbose_name='Período letivo'),
        ),
    ]