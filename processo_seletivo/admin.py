from django.contrib import admin
from .models import ProcessoSeletivo
from .models import Oferta

class OfertaInline(admin.TabularInline):
    model = Oferta

class ProcessoSeletivoAdmin(admin.ModelAdmin):
    inlines = [
        OfertaInline,
    ]
    # list_display = ['identificacao', 'ano_letivo', 'periodo_letivo', 'polo']
    # search_fields = ['id','identificacao', 'ano_letivo', 'periodo_letivo', 'polo']


admin.site.register(ProcessoSeletivo, ProcessoSeletivoAdmin)
