from django.contrib import admin
from .models import ProcessoSeletivo


class ProcessoSeletivoAdmin(admin.ModelAdmin):
    list_display = ['identificacao', 'ano_letivo', 'periodo_letivo', 'polo']
    search_fields = ['id','identificacao', 'ano_letivo', 'periodo_letivo', 'polo']


admin.site.register(ProcessoSeletivo, ProcessoSeletivoAdmin)
