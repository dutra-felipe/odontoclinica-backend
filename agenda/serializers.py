from rest_framework import serializers
from agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

    def validate(self, data):
        hora_inicio = data.get('hora_inicio')
        hora_fim = data.get('hora_fim')
        dentista = data.get('dentista')
        dia_semana = data.get('dia_semana')

        if hora_inicio >= hora_fim:
            raise serializers.ValidationError("A hora de início deve ser menor que a hora de término.")

        # Verifica se já existe agenda para o dentista nesse dia da semana
        qs = Agenda.objects.filter(dentista=dentista, dia_semana=dia_semana)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Esse dentista já possui uma agenda nesse dia da semana.")

        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['dentista'] = instance.dentista.nome
        return rep
