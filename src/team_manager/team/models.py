from django.db import models
from player.models import Player


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Player, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()
