# Generated by Django 2.1.1 on 2018-09-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dominio', '0004_merge_20180925_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formaingresso',
            options={'verbose_name': 'Forma de ingresso', 'verbose_name_plural': 'Formas de ingresso'},
        ),
        migrations.AlterModelOptions(
            name='nivelensino',
            options={'ordering': ['nome'], 'verbose_name': 'Nível de ensino', 'verbose_name_plural': 'Níveis de ensino'},
        ),
        migrations.AlterModelOptions(
            name='orgaoemissor',
            options={'ordering': ['nome'], 'verbose_name': 'Órgão emissor', 'verbose_name_plural': 'Órgãos emissores'},
        ),
        migrations.AlterModelOptions(
            name='paisorigem',
            options={'ordering': ['nome'], 'verbose_name': 'Pais de origem', 'verbose_name_plural': 'Paises de origem'},
        ),
        migrations.AlterModelOptions(
            name='tipocertidao',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo de certidão', 'verbose_name_plural': 'Tipos de certidões'},
        ),
        migrations.AlterModelOptions(
            name='tipodocumento',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo de documento', 'verbose_name_plural': 'Tipos de documentos'},
        ),
        migrations.AlterModelOptions(
            name='tipoinstituicao',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo de instituição', 'verbose_name_plural': 'Tipos de instituições'},
        ),
        migrations.AlterModelOptions(
            name='unidadefederativa',
            options={'ordering': ['nome'], 'verbose_name': 'Unidade federativa', 'verbose_name_plural': 'Unidades federativas'},
        ),
        migrations.AlterModelOptions(
            name='zonaresidencial',
            options={'ordering': ['nome'], 'verbose_name': 'Zona residencial', 'verbose_name_plural': 'Zonas residenciais'},
        ),
    ]
