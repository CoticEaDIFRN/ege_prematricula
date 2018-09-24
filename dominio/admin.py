from django.contrib import admin

from .models import Sexo
from .models import EstadoCivil
from .models import Raca
from .models import TipoSanguineo
from .models import TipoInstituicao


admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(Raca)
admin.site.register(TipoSanguineo)
admin.site.register(TipoInstituicao)
