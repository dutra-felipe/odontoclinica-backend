from rest_framework import serializers
from orcamentos.models import Orcamento
from paciente_tratamentos.models import PacienteTratamento
from paciente_tratamentos.serializers import PacienteTratamentoSerializer


class OrcamentoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.CharField(source='paciente.nome')
    tratamentos = PacienteTratamentoSerializer(many=True)
    valor_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Orcamento
        fields = '__all__'

    def create(self, validated_data):
        tratamentos_data = validated_data.pop('tratamentos')
        orcamento = Orcamento.objects.create(**validated_data)
        
        for tratamento_data in tratamentos_data:
            paciente_tratamento = PacienteTratamento.objects.get(id=tratamento_data.get('id'))
            orcamento.tratamentos.add(paciente_tratamento)
        
        # save() do models já calculará o valor_total
        orcamento.save()

        return orcamento
