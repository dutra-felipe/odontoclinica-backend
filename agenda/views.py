from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer 
from django_filters.rest_framework import DjangoFilterBackend

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #permission_classes = [IsAuthenticated]  # Você pode customizar depois com IsAdminUser ou uma permissão própria
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['dia_semana', 'dentista']
    search_fields = ['dentista__nome']
    ordering_fields = ['dia_semana', 'hora_inicio', 'hora_fim']
    ordering = ['dia_semana', 'hora_inicio']
