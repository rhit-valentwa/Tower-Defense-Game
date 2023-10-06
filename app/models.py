from django.db import models

class AvailablePlayer(models.Model):
    id = models.AutoField(primary_key=True)
    game_id = models.TextField()
    wants_to_attack = models.BooleanField(default=True)