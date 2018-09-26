# Generated by Django 2.1.1 on 2018-09-26 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0005_auto_20180925_1428'),
        ('processo_seletivo', '0007_auto_20180926_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='processoseletivo',
            name='forma_ingresso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dominio.FormaIngresso'),
            preserve_default=False,
        ),
    ]
