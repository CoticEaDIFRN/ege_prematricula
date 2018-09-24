from django.db import models
from django.utils.translation import gettext_lazy as _

class Base(models.Model):
    label = 'Nome'
    nome = models.CharField(_(label), max_length=200, null=False)

    label = 'Código SUAP'
    codigo_suap = models.CharField(_(label), max_length=200, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Sexo(Base):
    class Meta:
        verbose_name = _('Sexo')
        verbose_name_plural = _('Sexo')
        ordering = ['nome']


class EstadoCivil(Base):
    class Meta:
        verbose_name = _('Estado Civil')
        verbose_name_plural = _('Estado Civil')
        ordering = ['nome']


class Raca(Base):
    class Meta:
        verbose_name = _('Raça')
        verbose_name_plural = _('Raça')
        ordering = ['nome']


class TipoSanguineo(Base):
    class Meta:
        verbose_name = _('Tipo Sanguíneo')
        verbose_name_plural = _('Tipo Sanguíneo')
        ordering = ['nome']