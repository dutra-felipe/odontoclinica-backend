from rest_framework import serializers
from paciente_tratamentos.models import PacienteTratamento


class PacienteTratamentoSerializer(serializers.ModelSerializer):
    tratamento_nome = serializers.CharField(source='tratamento.nome')
    tratamento_valor = serializers.DecimalField(source='tratamento.valor', max_digits=10, decimal_places=2)

    class Meta:
        model = PacienteTratamento
        fields = '__all__'
