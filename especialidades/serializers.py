from rest_framework import serializers
from especialidades.models import Especialidades

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'
