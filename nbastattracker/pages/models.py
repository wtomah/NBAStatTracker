from django.db import models

# Create your models here.

class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    points_per_game =models.FloatField()
    rebounds_per_game = models.FloatField()
    assists_per_game = models.FloatField()
    STATUS_CHOICES = [
        (1, 'Available'),
        (2, 'Day-to-Day'),
        (3, 'Out'),
    ]

    availability = models.IntegerField(choices=STATUS_CHOICES, default=1)

def __str__(self):
    return f"{self.firstname} {self.lastname}"