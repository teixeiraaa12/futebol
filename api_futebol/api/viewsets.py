from rest_framework import viewsets
from api_futebol import models
from api_futebol.api import serializers

class TimesViewset (viewsets.ModelViewSet):
    serializer_class = serializers.TimesSerializer
    queryset =models.Times.objects.all()

class PartidaViewset (viewsets.ModelViewSet):
    serializer_class = serializers.PartidaSerializer
    queryset = models.Partida.objects.all()
