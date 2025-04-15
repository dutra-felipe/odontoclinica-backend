from django.contrib import admin
from .models import Agenda


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('dentista', 'dia_semana', 'hora_inicio', 'hora_fim')
    search_fields = ('dentista__nome',)
    list_filter = ('dentista', 'dia_semana')
    ordering = ('dentista', 'dia_semana')
    list_per_page = 10

