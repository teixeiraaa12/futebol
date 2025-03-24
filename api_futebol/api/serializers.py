from rest_framework import serializers
from api_futebol import models

class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Times
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador do time'},
            'nome': {'help_text': 'Nome do time'},
        }

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partida
        fields = "__all__"
        extra_kwargs = {
            'id': {'help_text': 'Identificador da partida'},
            'time1': {'help_text': 'ID do primeiro time. Buscar o ID no GET da API de Times'},
            'time2': {'help_text': 'ID do segundo time. Buscar o ID no GET da API de Times'},
            'data': {'help_text': 'Data da partida'},
            'horario': {'help_text': 'Horário da partida'},
            'placartime1': {'help_text': 'Placar do primeiro time'},
            'placartime2': {'help_text': 'Placar do segundo time'},
            'estadio': {'help_text': 'Nome do estádio onde ocorrerá a partida'},
            'juiz': {'help_text': 'Nome do juiz responsável pela partida'},
            'quantcartoes': {'help_text': 'Quantidade total de cartões aplicados na partida'},
        }
