from django.db import models
from django.utils.translation import gettext_lazy as _


class ProcessoSeletivo(models.Model):
    PERIODO = (
        (1, '1º Período'),
        (2, '2º Período'),
    )
    identificacao = models.CharField(_('Identificação'), max_length=256)
    ano_letivo = models.PositiveIntegerField(_('Ano letivo'))
    periodo_letivo = models.PositiveIntegerField(_('Período letivo'), choices=PERIODO)
    turno = models.ForeignKey('dominio.Turno', on_delete=models.CASCADE)
    conclusao_intercambio = models.DateField(_('Conclusão do intercâmbio'), auto_now=False, auto_now_add=False)
    matriz_curso = models.CharField(_('Matriz/Curso'), max_length=256)
    linha_pesquisa = models.CharField(_('Linha de pesquisa'), max_length=256)
    aluno_especial = models.BooleanField(_('Aluno especial?'))
    numero_pasta = models.CharField(_('Número da pasta'),  max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=2000, null=True, blank=True)
    observacao = models.TextField(_('Observação'), max_length=2000, null=True, blank=True)


    def __str__(self):
        return self.identificacao

    class Meta:
        verbose_name = _('Processo seletivo')
        verbose_name_plural = _('Processos seletivos')
        ordering = ['identificacao']