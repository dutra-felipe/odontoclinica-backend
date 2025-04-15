from django.contrib import admin
from consultas.models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'dentista', 'data', 'hora', 'status', 'observacoes')
    search_fields = ('paciente__nome', 'dentista__nome')
    list_filter = ('status', 'data')
    ordering = ('data', 'hora')
    list_per_page = 10

