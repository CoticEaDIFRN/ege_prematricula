from django.contrib import admin

from .models import Sexo
from .models import EstadoCivil
from .models import Raca
from .models import TipoSanguineo
from .models import TipoInstituicao
from .models import NivelEnsino
from .models import UnidadeFederativa
from .models import PaisOrigem
from .models import OrgaoEmissor
from .models import TipoCertidao
from .models import ZonaResidencial
from .models import TipoDocumento
from .models import Convenio
from .models import FormaIngresso
from .models import Polo
from .models import Turno
from .models import Campus
from .models import Curso

admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(Raca)
admin.site.register(TipoSanguineo)
admin.site.register(TipoInstituicao)
admin.site.register(NivelEnsino)
admin.site.register(UnidadeFederativa)
admin.site.register(PaisOrigem)
admin.site.register(OrgaoEmissor)
admin.site.register(TipoCertidao)
admin.site.register(ZonaResidencial)
admin.site.register(TipoDocumento)
admin.site.register(Convenio)
admin.site.register(FormaIngresso)
admin.site.register(Polo)
admin.site.register(Turno)
admin.site.register(Campus)
admin.site.register(Curso)
