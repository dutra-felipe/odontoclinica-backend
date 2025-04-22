from django.contrib import admin
from .models import Tratamento


@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_padrao')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10
