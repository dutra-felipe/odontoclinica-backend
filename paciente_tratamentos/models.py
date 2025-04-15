from django.db import models
from pacientes.models import Paciente
from tratamentos.models import Tratamento

class PacienteTratamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamento = models.ForeignKey(Tratamento, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('agendado', 'Agendado'), ('em andamento', 'Em andamento'), ('finalizado', 'Finalizado')])

    def __str__(self):
        return f"{self.paciente.nome} - {self.tratamento.nome} ({self.status})"
