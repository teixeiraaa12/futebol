from rest_framework import viewsets
from api_futebol import models
from api_futebol.api import serializers
from drf_yasg.utils import swagger_auto_schema

class TimesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TimesSerializer
    queryset = models.Times.objects.all()

    @swagger_auto_schema(
        operation_description="Lista todos os times",
        responses={200: serializers.TimesSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo time",
        responses={201: "Time criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o time conforme o ID informado",
        responses={200: "Time encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera o time conforme informado",
        responses={201: "Time alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta um time",
        responses={204: "Time deletado com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PartidaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PartidaSerializer
    queryset = models.Partida.objects.all()

    @swagger_auto_schema(
        operation_description="Lista todas as partidas",
        responses={200: serializers.PartidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria uma nova partida",
        responses={201: "Partida criada com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna a partida conforme o ID informado",
        responses={200: "Partida encontrada"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Altera a partida conforme informado",
        responses={201: "Partida alterada com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta uma partida",
        responses={204: "Partida deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

