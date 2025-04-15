from django.db import models
from pacientes.models import Paciente
from paciente_tratamentos.models import PacienteTratamento


class Orcamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamentos = models.ManyToManyField(PacienteTratamento)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    validade = models.DateField()

    def save(self, *args, **kwargs):
        total = sum([tratamento.tratamento.valor for tratamento in self.tratamentos.all()])
        self.valor_total = total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orçamento para {self.paciente.nome} - {self.valor_total}"
