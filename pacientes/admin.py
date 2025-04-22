from django.contrib import admin
from pacientes.models import Paciente


@admin.register(Paciente)
class PacienteAdmn(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'endereco', 'telefone', 'email', 'convenio', 'num_carteirinha', 'ativo')
    search_fields = ('nome', 'cpf', 'telefone', 'email', 'convenio', 'num_carteirinha')
    list_filter = ('ativo', 'convenio')
    ordering = ('nome',)
    list_per_page = 10
