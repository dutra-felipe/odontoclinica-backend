from django.db import models
from dentistas.models import Dentista


class Agenda(models.Model):
    DIA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
    ]
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DIA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    
    def __str__(self):
        return f"{self.dentista.nome} - {self.dia_semana} {self.hora_inicio}-{self.hora_fim}"
