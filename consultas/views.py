from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from consultas.models import Consulta
from consultas.serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'paciente'):
            return Consulta.objects.filter(paciente=user.paciente)
        elif hasattr(user, 'dentista'):
            return Consulta.objects.filter(dentista=user.dentista)
        else:
            return Consulta.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'paciente'):
            serializer.save(paciente=user.paciente)
        else:
            serializer.save()
