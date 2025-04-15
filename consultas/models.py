from django.db import models
from pacientes.models import Paciente
from dentistas.models import Dentista

class Consulta(models.Model):
    class Status(models.TextChoices):
        AGENDADA = 'agendada', 'Agendada'
        CANCELADA = 'cancelada', 'Cancelada'
        REALIZADA = 'realizada', 'Realizada'

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AGENDADA)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora} com {self.dentista.nome}"
