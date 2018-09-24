from django.contrib import admin

from .models import Sexo
from .models import EstadoCivil
from .models import Raca
from .models import TipoSanguineo


admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(Raca)
admin.site.register(TipoSanguineo)