# Generated by Django 2.1.1 on 2018-09-25 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dominio.Base')),
            ],
            options={
                'verbose_name': 'Convênio',
                'verbose_name_plural': 'Convênios',
                'ordering': ['nome'],
            },
            bases=('dominio.base',),
        ),
        migrations.CreateModel(
            name='FormaIngresso',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dominio.Base')),
            ],
            options={
                'verbose_name': 'Forma de Ingresso',
                'verbose_name_plural': 'Formas de Ingresso',
                'ordering': ['nome'],
            },
            bases=('dominio.base',),
        ),
        migrations.AlterModelOptions(
            name='tipodocumento',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo de Documento', 'verbose_name_plural': 'Tipos de Documentos'},
        ),
    ]
