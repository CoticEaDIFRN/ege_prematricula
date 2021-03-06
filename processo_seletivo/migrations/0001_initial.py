# Generated by Django 2.1.1 on 2018-09-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoSeletivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=256, verbose_name='Identificação')),
                ('ano_letivo', models.PositiveIntegerField(max_length=200, verbose_name='Ano letivo')),
                ('periodo_letivo', models.PositiveIntegerField(choices=[(1, '1'), (2, '2')], max_length=1, verbose_name='Período letivo')),
                ('conclusao_intercambio', models.DateField(verbose_name='Conclusão do intercâmbio')),
                ('matriz_curso', models.TextField(max_length=256, verbose_name='Matriz \\ Curso')),
                ('linha_pesquisa', models.TextField(max_length=256, verbose_name='Linha de pesquisa')),
                ('aluno_especial', models.BooleanField(verbose_name='Aluno especial?')),
                ('numero_pasta', models.CharField(max_length=100, verbose_name='Número da pasta')),
                ('descricao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Descrição')),
                ('observacao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Processo seletivo',
                'verbose_name_plural': 'Processos seletivos',
                'ordering': ['identificacao'],
            },
        ),
    ]
