from django.db import models
import markdown2


class PlayerManager(models.Manager):
    def get_players_waiting(self):
        return Player.objects.filter(waiting=True)


    def get_percentage_moved(self):
        try:
            total = Player.objects.count()
            moved = Player.objects.filter(waiting=False).count()
            return 100 * float(moved) / float(total)
        except ZeroDivisionError:
            return 0


class Player(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    country = models.CharField(max_length=200, blank=True, verbose_name="Country")
    email = models.CharField(max_length=200, blank=True, verbose_name="Email")
    image = models.CharField(max_length=500, blank=True, verbose_name="Image URL")
    description = models.TextField(blank=True, verbose_name="Description")
    waiting = models.BooleanField(default=True, verbose_name="Waiting for Move")

    objects = PlayerManager()

    def __unicode__(self):
        return self.name


class UpdateManager(models.Manager):
    def get_latest(self):
        try:
            return Update.objects.all().order_by('-date')[0]
        except IndexError:
            return None


    def get_by_id(self, id):
        return Update.objects.get(id=id)


class Update(models.Model):
    date = models.DateTimeField(db_index=True, auto_created=True, blank=True, verbose_name="Date")
    title = models.CharField(max_length=200, verbose_name="Title")
    season = models.CharField(max_length=200, verbose_name="Season")
    body = models.TextField(verbose_name="Body")

    objects = UpdateManager()

    # markdown2.markdown(self.body)
    def save(self, *args, **kwargs):
        self.body = markdown2.markdown(self.body)
        super(Update, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title
