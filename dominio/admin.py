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
