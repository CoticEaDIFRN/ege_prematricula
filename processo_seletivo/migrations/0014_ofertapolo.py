# Generated by Django 2.1.1 on 2018-09-26 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0006_auto_20180926_1345'),
        ('processo_seletivo', '0013_auto_20180926_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfertaPolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo_seletivo.Oferta')),
                ('polo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dominio.Polo')),
            ],
        ),
    ]
