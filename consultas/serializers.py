from rest_framework import serializers
from consultas.models import Consulta
from agenda.models import Agenda
from consultas.models import Consulta as ConsultaModel

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate(self, data):
        data_consulta = data.get('data')
        hora_inicio = data.get('hora_inicio')
        hora_fim = data.get('hora_fim')
        dentista = data.get('dentista')

        if not data_consulta or not hora_inicio or not hora_fim or not dentista:
            raise serializers.ValidationError("Todos os campos obrigatórios devem ser preenchidos.")

        dia_semana = data_consulta.weekday()  # 0=segunda  6=domingo
        try:
            agenda = Agenda.objects.get(dentista=dentista, dia_semana=dia_semana)
        except Agenda.DoesNotExist:
            raise serializers.ValidationError("Dentista não possui agenda para esse dia da semana.")

        if not (agenda.hora_inicio <= hora_inicio <= agenda.hora_fim):
            raise serializers.ValidationError("Hora de início fora da agenda do dentista.")
        if not (agenda.hora_inicio <= hora_fim <= agenda.hora_fim):
            raise serializers.ValidationError("Hora de término fora da agenda do dentista.")
        if hora_inicio >= hora_fim:
            raise serializers.ValidationError("Hora de início deve ser menor que a de término.")

        conflitos = ConsultaModel.objects.filter(
            dentista=dentista,
            data=data_consulta,
            hora_inicio__lt=hora_fim,
            hora_fim__gt=hora_inicio
        )
        if self.instance:
            conflitos = conflitos.exclude(pk=self.instance.pk)

        if conflitos.exists():
            raise serializers.ValidationError("Dentista já possui uma consulta nesse horário.")

        return data
