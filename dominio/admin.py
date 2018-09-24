from django.contrib import admin

from .models import Sexo

class SexoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'created_at']
    search_fields = ['id','nome']


admin.site.register(Sexo)
