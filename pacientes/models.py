from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=15, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    convenio = models.CharField(max_length=100)
    num_carteirinha = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
