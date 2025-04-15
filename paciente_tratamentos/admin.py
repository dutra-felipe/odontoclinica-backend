from django.contrib import admin
from .models import PacienteTratamento


@admin.register(PacienteTratamento)
class PacienteTratamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'tratamento', 'data_inicio', 'data_fim', 'status')
    search_fields = ('paciente__nome', 'tratamento__nome')
    list_filter = ('status', 'data_inicio')
    list_per_page = 20
