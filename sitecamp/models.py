from django.db import models

class Lieux(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    lien = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"