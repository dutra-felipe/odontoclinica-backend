from django.db import models


class Especialidades(models.Model):
    nome_especialidade = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome_especialidade
