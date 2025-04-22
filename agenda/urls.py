from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agenda.views import AgendaViewSet

router = DefaultRouter()
router.register(r'agenda', AgendaViewSet, basename='agenda')

urlpatterns = [
    path('', include(router.urls)),
]
