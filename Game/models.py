from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    country = models.CharField(max_length=200, verbose_name="Country")
    email = models.CharField(max_length=200, verbose_name="Email")
    description = models.TextField(verbose_name="Description")

    def __unicode__(self):
        return self.name


class Update(model.Model):
    title = models.CharField(max_length=200, verbose_name="Title")


    def __unicode__(self):
        return self.title
