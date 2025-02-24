from django.db import models
from django.core.validators import MaxValueValidator

class Times(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Partida(models.Model):
    time1 = models.ForeignKey(Times, on_delete=models.DO_NOTHING, related_name="partidas_como_time1")
    time2 = models.ForeignKey(Times, on_delete=models.DO_NOTHING, related_name="partidas_como_time2")
    data = models.DateField()
    horario = models.TimeField()
    placartime1 = models.IntegerField()
    placartime2 = models.IntegerField()
    estadio = models.CharField(max_length=50)
    juiz = models.CharField(max_length=30)
    quantcartoes = models.IntegerField(validators=[MaxValueValidator(99)])

    def __str__(self):
        return f"{self.time1} vs {self.time2} - {self.data}"







