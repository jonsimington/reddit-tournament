from django.db import models

from django.contrib.auth.models import User

class Tournament(models.Model):
    name = models.TextField(max_length=50)
    
    
    STRUCTURE_CHOICES = (
        ("S.E.", "Single Elimination"),
        ("D.E.", "Double Elimination"),
    )
    structure = models.TextField(choices=STRUCTURE_CHOICES, max_length=20,)

    # games is implicit

    round_length = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    start_date = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Game(models.Model):
    tournament = models.ForeignKey('Tournament')
    round_num = models.IntegerField()
    player1 = models.OneToOneField(User, related_name="player1")
    player2 = models.OneToOneField(User, related_name="player2")
    winner = models.TextField(default="", max_length=20)
