from django.db import models
from django.utils.translation import gettext_lazy as _


class ProcessoSeletivo(models.Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )
    identificacao = models.CharField(_('Identificação'), max_length=256)
    uo = models.CharField(_('Unidade organizacional'),  max_length=100)
    numero_ano = models.CharField(_('Número / Ano'),  max_length=100)
    ano_letivo = models.PositiveIntegerField(_('Ano letivo'))
    periodo_letivo = models.PositiveIntegerField(_('Período letivo'), choices=PERIODO)
    url = models.URLField(_('Endereço do edital'),  max_length=300)
    descricao = models.TextField(_('Descrição'), max_length=2000, null=True, blank=True)

    # forma_ingresso = models.ForeignKey('dominio.FormaIngresso', on_delete=models.CASCADE)
    # convenio = models.ForeignKey('dominio.Convenio', on_delete=models.CASCADE,null=True, blank=True)
    # conclusao_intercambio = models.DateField(_('Conclusão do intercâmbio'), auto_now=False, auto_now_add=False)
    # matriz_curso = models.CharField(_('Matriz/Curso'), max_length=256)
    # linha_pesquisa = models.CharField(_('Linha de pesquisa'), max_length=256)
    # aluno_especial = models.BooleanField(_('Aluno especial?'))
    # numero_pasta = models.CharField(_('Número da pasta'),  max_length=100)
    # observacao = models.TextField(_('Observação'), max_length=2000, null=True, blank=True)


    def __str__(self):
        return self.identificacao

    class Meta:
        verbose_name = _('Processo seletivo')
        verbose_name_plural = _('Processos seletivos')
        ordering = ['identificacao']


class Oferta(models.Model):
    nome = models.CharField(_('Nome'), max_length=256)
    processo_seletivo = models.ForeignKey(ProcessoSeletivo, on_delete=models.CASCADE)
    campus = models.ForeignKey('dominio.Campus', on_delete=models.CASCADE)
    polo = models.ForeignKey('dominio.Polo', on_delete=models.CASCADE)
    curso = models.ForeignKey('dominio.Curso', on_delete=models.CASCADE)
    turno = models.ForeignKey('dominio.Turno', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')
        ordering = ['nome']