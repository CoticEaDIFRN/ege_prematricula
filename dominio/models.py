from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    nome = models.CharField(_('Nome'), max_length=200)
    codigo_suap = models.CharField(_('Código SUAP'), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Sexo(Base):
    class Meta:
        verbose_name = _('Sexo')
        verbose_name_plural = _('Sexos')
        ordering = ['nome']


class EstadoCivil(Base):
    class Meta:
        verbose_name = _('Estado civil')
        verbose_name_plural = _('Estados civis')
        ordering = ['nome']


class Raca(Base):
    class Meta:
        verbose_name = _('Raça')
        verbose_name_plural = _('Raças')
        ordering = ['nome']


class TipoSanguineo(Base):
    class Meta:
        verbose_name = _('Tipo sanguíneo')
        verbose_name_plural = _('Tipos sanguíneos')
        ordering = ['nome']


class TipoInstituicao(Base):
    class Meta:
        verbose_name = _('Tipo de Instituição')
        verbose_name_plural = _('Tipos de Instituições')
        ordering = ['nome']


class NivelEnsino(Base):
    class Meta:
        verbose_name = _('Nível de Ensino')
        verbose_name_plural = _('Níveis de Ensino')
        ordering = ['nome']
  
  
class UnidadeFederativa(Base):
    class Meta:
        verbose_name = _('Unidade Federativa')
        verbose_name_plural = _('Unidades Federativas')
        ordering = ['nome']


class PaisOrigem(Base):
    class Meta:
        verbose_name = _('Pais de Origem')
        verbose_name_plural = _('Paises de Origem')
        ordering = ['nome']


class OrgaoEmissor(Base):
    class Meta:
        verbose_name = _('Órgão Emissor')
        verbose_name_plural = _('Órgãos Emissores')
        ordering = ['nome']


class TipoCertidao(Base):
    class Meta:
        verbose_name = _('Tipo de Certidão')
        verbose_name_plural = _('Tipos de Certidões')
        ordering = ['nome']


class ZonaResidencial(Base):
    class Meta:
        verbose_name = _('Zona Residencial')
        verbose_name_plural = _('Zonas Residenciais')
        ordering = ['nome']


class TipoDocumento(Base):
    class Meta:
        verbose_name = _('Tipo de Documento')
        verbose_name_plural = _('Tipos de Documentos')
        ordering = ['nome']


class Convenio(Base):
    class Meta:
        verbose_name = _('Convênio')
        verbose_name_plural = _('Convênios')
        ordering = ['nome']


class FormaIngresso(Base):
    class Meta:
        verbose_name = _('Forma de Ingresso')
        verbose_name_plural = _('Formas de Ingresso')


class Polo(Base):
    class Meta:
        verbose_name = _('Polo')
        verbose_name_plural = _('Polos')
        ordering = ['nome']


class Turno(Base):
    class Meta:
        verbose_name = _('Turno')
        verbose_name_plural = _('Turnos')
        ordering = ['nome']
