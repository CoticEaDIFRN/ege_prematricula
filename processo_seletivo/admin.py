from django.contrib import admin
from .models import ProcessoSeletivo
from .models import Oferta
from .models import Arquivo


class OfertaInline(admin.TabularInline):
    model = Oferta
    extra = 1


class ArquivoInline(admin.TabularInline):
    model = Arquivo
    extra = 1


class ProcessoSeletivoAdmin(admin.ModelAdmin):
    inlines = [
        OfertaInline,
        ArquivoInline
    ]
    # list_display = ['identificacao', 'ano_letivo', 'periodo_letivo']
    # search_fields = ['id','identificacao', 'ano_letivo', 'periodo_letivo']


admin.site.register(ProcessoSeletivo, ProcessoSeletivoAdmin)
