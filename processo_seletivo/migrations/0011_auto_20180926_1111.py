# Generated by Django 2.1.1 on 2018-09-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processo_seletivo', '0010_processoseletivo_convenio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processoseletivo',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dominio.Convenio'),
        ),
    ]
