from django.conf.urls import patterns, url
from django.contrib import admin

from .models import *

class TournamentInline(admin.TabularInline):
    """ Tournament inline options """
    model = Tournament
    fields = ("name", "structure", "round_length", "created", "start_date",)

class TournamentAdmin(admin.ModelAdmin):
    """ Tournament admin model """
    list_display = ("name", "structure", "round_length", "created", "start_date",)
    search_fields = ("name", "structure")

class GameInline(admin.TabularInline):
    """ Game inline options """
    model = Game
    fields = ("tournament", "round_num", "player1", "player2", "winner",)

class GameAdmin(admin.ModelAdmin):
    """ Game Admin Model """
    list_display = ("tournament", "round_num", "player1", "player2", "winner",)
    search_fields = ("tournament", "round_num", "player1", "player2", "winner",)
    

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Game, GameAdmin)
