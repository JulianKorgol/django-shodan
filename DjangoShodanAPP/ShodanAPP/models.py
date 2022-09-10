from django.db import models

class Configuration(models.Model):
    ShodanAPIKey = models.CharField(max_length=100)

    def __str__(self):
        return self.ShodanAPIKey
