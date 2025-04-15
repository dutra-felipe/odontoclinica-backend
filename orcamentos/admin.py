from django.contrib import admin
from orcamentos.models import Orcamento


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'valor_total', 'validade')
    search_fields = ('paciente__nome',)
    ordering = ('paciente__nome',)
    list_per_page = 10
