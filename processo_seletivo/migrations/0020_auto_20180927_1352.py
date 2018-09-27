# Generated by Django 2.1.1 on 2018-09-27 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processo_seletivo', '0019_arquivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oferta',
            options={'verbose_name': 'Oferta', 'verbose_name_plural': 'Ofertas'},
        ),
        migrations.AlterModelOptions(
            name='processoseletivo',
            options={'verbose_name': 'Processo seletivo', 'verbose_name_plural': 'Processos seletivos'},
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='processoseletivo',
            name='identificacao',
        ),
        migrations.AlterField(
            model_name='oferta',
            name='polo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dominio.Polo'),
        ),
        migrations.AlterField(
            model_name='processoseletivo',
            name='descricao',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='processoseletivo',
            name='url',
            field=models.URLField(help_text='Informe o LINK onde está o edital', max_length=300, verbose_name='URL'),
        ),
    ]
