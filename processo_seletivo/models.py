from django.db import models
from django.utils.translation import gettext_lazy as _


class ProcessoSeletivo(models.Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )
    uo = models.CharField(_('Unidade organizacional'),  max_length=100, help_text='Ex.: DG-EAD/IFRN')
    numero_ano = models.CharField(_('Número / Ano'),  max_length=100, help_text='Digite o número e o ano do edital. Ex.: 36/2018')
    ano_letivo = models.PositiveIntegerField(_('Ano letivo'), help_text='Digite o ano')
    periodo_letivo = models.PositiveIntegerField(_('Período letivo'), choices=PERIODO)
    url = models.URLField(_('URL'),  max_length=300, help_text='Informe o LINK onde está o edital')
    descricao = models.CharField(_('Descrição'), max_length=256, null=True, blank=True)

    def __str__(self):
        return self.identificacao

    @property
    def identificacao(self):
        return "Edital %s (%s)" % (self.numero_ano, self.uo)

    class Meta:
        verbose_name = _('Processo seletivo')
        verbose_name_plural = _('Processos seletivos')


class Oferta(models.Model):
    processo_seletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    campus = models.ForeignKey('dominio.Campus', on_delete=models.CASCADE)
    curso = models.ForeignKey('dominio.Curso', on_delete=models.CASCADE)
    turno = models.ForeignKey('dominio.Turno', on_delete=models.CASCADE)
    polo = models.ForeignKey('dominio.Polo', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

    @property
    def nome(self):
        return "%s > %s > %s" % (self.campus, self.curso, self.turno)

    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')


class Arquivo(models.Model):
    arquivo = models.FileField(_('Arquivo de importação'), help_text='Informe o arquivo de importação')
    processo_seletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.arquivo)

    class Meta:
        verbose_name = _('Arquivo de importação')
        verbose_name_plural = _('Arquivos de importações')
        ordering = ['arquivo']


class Selecionado(models.Model):
    estado_civil = models.ForeignKey('dominio.EstadoCivil', on_delete=models.CASCADE,null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=True, blank=True)
    forma_ingresso = models.ForeignKey('dominio.FormaIngresso', on_delete=models.CASCADE)
    convenio = models.ForeignKey('dominio.Convenio', on_delete=models.CASCADE,null=True, blank=True)
    foto = models.FileField('Arquivo de importação', unique=True, null=True, blank=True)
    nome = models.CharField('Nome', max_length=200, unique=True, null=True, blank=True)
    nome_social = models.CharField('Nome social', max_length=200, unique=True, null=True, blank=True)
    sexo = models.ForeignKey('dominio.sexo', on_delete=models.CASCADE, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
    nome_pai = models.CharField('Nome do pai', max_length=200, unique=True, null=True, blank=True)
    pai_falecido = models.CharField('Pai falecido?', max_length=200, unique=True, null=True, blank=True)
    nome_mae = models.CharField('Nome da mãe', max_length=200, unique=True, null=True, blank=True)
    nome_resp = models.CharField('Nome do responsável', max_length=200, unique=True, null=True, blank=True)
    email_resp = models.EmailField('E-mail do responsável', max_length=50, unique=True, null=True, blank=True)

    # conclusao_intercambio = models.DateField(_('Conclusão do intercâmbio'), auto_now=False, auto_now_add=False)
    # matriz_curso = models.CharField(_('Matriz/Curso'), max_length=256)
    # linha_pesquisa = models.CharField(_('Linha de pesquisa'), max_length=256)
    # aluno_especial = models.BooleanField(_('Aluno especial?'))
    # numero_pasta = models.CharField(_('Número da pasta'),  max_length=100)
    # observacao = models.TextField(_('Observação'), max_length=2000, null=True, blank=True)
