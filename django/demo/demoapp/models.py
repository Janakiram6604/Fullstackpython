from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    reservation_time = models.DateTimeField(auto_now_add=True)
    party_size = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.party_size})"
