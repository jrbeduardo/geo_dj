from django.db import models

# Create your models here.

class Visitor(models.Model):
    ip = models.GenericIPAddressField()
    create = models.DateTimeField(auto_now_add=True)
    latitud = models.DecimalField(max_digits=11, decimal_places=7, default = 19.4284700 )
    longitud = models.DecimalField(max_digits=11, decimal_places=7, default = -99.1276600)
    def __str__(self):
        return self.ip
    class Admin:
        fields = ('ip', 'latitud', 'longitud')

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance =  models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Distance from {self.location} to {self.destination}"
