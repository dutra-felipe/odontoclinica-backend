from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consultas.views import ConsultaViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet, basename='consultas')

urlpatterns = [
    path('', include(router.urls)),
]