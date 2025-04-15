from django.db import models
from pacientes.models import Paciente
from dentistas.models import Dentista


class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE, related_name='prontuarios')
    data = models.DateTimeField(auto_now_add=True)
    anotacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Prontuário de {self.paciente.nome} - {self.data.strftime('%d/%m/%Y')}"


class ImagemProntuario(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='prontuarios/')
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Imagem de {self.prontuario.paciente.nome} - {self.data_upload.strftime('%d/%m/%Y')}"
