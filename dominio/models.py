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


class TipoInstituicao(Base):
    class Meta:
        verbose_name = _('Tipo de Instituição')
        verbose_name_plural = _('Tipo de Instituição')
        ordering = ['nome']


class NivelEnsino(Base):
    class Meta:
        verbose_name = _('Nível de Ensino')
        verbose_name_plural = _('Nível de Ensino')
  
  
class UnidadeFederativa(Base):
    class Meta:
        verbose_name = _('Unidade Federativa')
        verbose_name_plural = _('Unidade Federativa')
        ordering = ['nome']


class PaisOrigem(Base):
    class Meta:
        verbose_name = _('Pais de Origem')
        verbose_name_plural = _('Pais de Origem')
        ordering = ['nome']


class OrgaoEmissor(Base):
    class Meta:
        verbose_name = _('Órgão Emissor')
        verbose_name_plural = _('Órgão Emissor')
        ordering = ['nome']


class TipoCertidao(Base):
    class Meta:
        verbose_name = _('Tipo de Certidão')
        verbose_name_plural = _('Tipo de Certidão')
        ordering = ['nome']


class ZonaResidencial(Base):
    class Meta:
        verbose_name = _('Zona Residencial')
        verbose_name_plural = _('Zona Residencial')
        ordering = ['nome']
        