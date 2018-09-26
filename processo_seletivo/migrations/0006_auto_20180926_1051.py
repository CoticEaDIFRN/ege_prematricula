# Generated by Django 2.1.1 on 2018-09-26 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0005_auto_20180925_1428'),
        ('processo_seletivo', '0005_auto_20180925_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='processoseletivo',
            name='turno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dominio.Turno'),
        ),
        migrations.AlterField(
            model_name='processoseletivo',
            name='periodo_letivo',
            field=models.PositiveIntegerField(choices=[(1, '1º Período'), (2, '2º Período')], verbose_name='Período letivo'),
        ),
    ]