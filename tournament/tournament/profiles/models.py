from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    # email is provided in the User model

    # Max length is 17 -> 12 chars for name, 5 for pound and 4-digit identifier
    battletag = models.TextField(max_length=17)
    reddit_username = models.TextField(max_length=15)

    # The list of tournaments that the user is registered for
    #tournaments = models.ManyToManyField(Tournament, related_name="tournaments")
