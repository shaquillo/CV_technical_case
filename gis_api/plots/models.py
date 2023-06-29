from django.contrib.gis.db import models

# Create your models here.

class Plot(models.Model):
    name = models.CharField(max_length=50)
    geometry = models.PolygonField()
    owner = models.ForeignKey('auth.User', related_name='plots', on_delete=models.CASCADE)
