from django.db import models


class Configuration(models.Model):
    ShodanAPIName = models.CharField(max_length=30, default='ShodanAPIKey')
    ShodanAPIKey = models.CharField(max_length=100)

    def __str__(self):
        return self.ShodanAPIName
