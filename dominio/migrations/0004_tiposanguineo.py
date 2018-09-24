# Generated by Django 2.1.1 on 2018-09-24 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0003_raca'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSanguineo',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dominio.Base')),
            ],
            options={
                'verbose_name': 'Tipo Sanguíneo',
                'verbose_name_plural': 'Tipo Sanguíneo',
                'ordering': ['nome'],
            },
            bases=('dominio.base',),
        ),
    ]
