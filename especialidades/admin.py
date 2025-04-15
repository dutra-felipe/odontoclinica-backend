from django.contrib import admin
from especialidades.models import Especialidades


@admin.register(Especialidades)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_especialidade')
    search_fields = ('nome_especialidade',)
    list_filter = ('nome_especialidade',)
    ordering = ('id',)
    list_per_page = 10

