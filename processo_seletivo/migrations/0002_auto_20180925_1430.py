# Generated by Django 2.1.1 on 2018-09-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo_seletivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processoseletivo',
            name='linha_pesquisa',
            field=models.CharField(max_length=256, verbose_name='Linha de pesquisa'),
        ),
        migrations.AlterField(
            model_name='processoseletivo',
            name='matriz_curso',
            field=models.CharField(max_length=256, verbose_name='Matriz \\ Curso'),
        ),
    ]
