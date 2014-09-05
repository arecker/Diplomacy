from django.db import models
import markdown2

class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    country = models.CharField(max_length=200, verbose_name="Country")
    email = models.CharField(max_length=200, verbose_name="Email")
    image = models.CharField(max_length=500, verbose_name="Image URL")
    description = models.TextField(verbose_name="Description")

    def __unicode__(self):
        return self.name


class Update(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    season = models.CharField(max_length=200, verbose_name="Season")
    body = models.TextField(verbose_name="Body")


    def body_to_html(self):
        return markdown2.markdown(self.body)


    def __unicode__(self):
        return self.title
