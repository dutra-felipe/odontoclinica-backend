from django.contrib import admin
from dentistas.models import Dentista


@admin.register(Dentista)
class PacienteAdmn(admin.ModelAdmin):
    list_display = ('nome', 'cro', 'especialidade', 'telefone', 'email')
    search_fields = ('nome', 'especialidade')
    list_filter = ('nome', 'especialidade')
    ordering = ('nome',)
    list_per_page = 10
