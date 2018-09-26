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
        verbose_name = _('Tipo de instituição')
        verbose_name_plural = _('Tipos de instituições')
        ordering = ['nome']


class NivelEnsino(Base):
    class Meta:
        verbose_name = _('Nível de ensino')
        verbose_name_plural = _('Níveis de ensino')
        ordering = ['nome']
  
  
class UnidadeFederativa(Base):
    class Meta:
        verbose_name = _('Unidade federativa')
        verbose_name_plural = _('Unidades federativas')
        ordering = ['nome']


class PaisOrigem(Base):
    class Meta:
        verbose_name = _('Pais de origem')
        verbose_name_plural = _('Paises de origem')
        ordering = ['nome']


class OrgaoEmissor(Base):
    class Meta:
        verbose_name = _('Órgão emissor')
        verbose_name_plural = _('Órgãos emissores')
        ordering = ['nome']


class TipoCertidao(Base):
    class Meta:
        verbose_name = _('Tipo de certidão')
        verbose_name_plural = _('Tipos de certidões')
        ordering = ['nome']


class ZonaResidencial(Base):
    class Meta:
        verbose_name = _('Zona residencial')
        verbose_name_plural = _('Zonas residenciais')
        ordering = ['nome']


class TipoDocumento(Base):
    class Meta:
        verbose_name = _('Tipo de documento')
        verbose_name_plural = _('Tipos de documentos')
        ordering = ['nome']


class Convenio(Base):
    class Meta:
        verbose_name = _('Convênio')
        verbose_name_plural = _('Convênios')
        ordering = ['nome']


class FormaIngresso(Base):
    class Meta:
        verbose_name = _('Forma de ingresso')
        verbose_name_plural = _('Formas de ingresso')
        ordering = ['nome']


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


class Campus(Base):
    class Meta:
        verbose_name = _('Campus')
        verbose_name_plural = _('Campi')
        ordering = ['nome']


class Curso(Base):
    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')
        ordering = ['nome']