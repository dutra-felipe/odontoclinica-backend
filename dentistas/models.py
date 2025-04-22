from django.db import models
from especialidades.models import Especialidades


class Dentista(models.Model):
    nome = models.CharField(max_length=150)
    cro = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"
