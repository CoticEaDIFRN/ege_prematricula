# Generated by Django 2.1.1 on 2018-09-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0009_orgaoemissor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCertidao',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dominio.Base')),
            ],
            options={
                'verbose_name': 'Tipo de Certidão',
                'verbose_name_plural': 'Tipo de Certidão',
                'ordering': ['nome'],
            },
            bases=('dominio.base',),
        ),
    ]
