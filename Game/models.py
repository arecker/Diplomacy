from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    country = models.CharField(max_length=200, verbose_name="Country")

    def __unicode__(self):
        return self.name
