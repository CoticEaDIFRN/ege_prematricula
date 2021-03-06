# Generated by Django 2.1.1 on 2018-09-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processo_seletivo', '0011_auto_20180926_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Nome')),
                ('processo_seletivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo_seletivo.ProcessoSeletivo')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
                'ordering': ['nome'],
            },
        ),
    ]
