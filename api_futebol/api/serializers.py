from rest_framework import serializers
from api_futebol import models

class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Times
        fields = "__all__"

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partida
        fields = "__all__"
