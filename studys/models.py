from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class classification(models.Model):
    category= models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Articles(models.Model):
    time = models.DateField('Date published')
    title = models.CharField(max_length=200)
    content = RichTextField()
    categorys = models.ForeignKey(classification,models.CASCADE)

    def __str__(self):
        return self.title

    def published_recently(self):
        return self.time >= timezone.now() -datetime.timedelta(days=1)


class Methods(models.Model):
    time = models.DateField('Date published')
    title = models.CharField(max_length=200)
    content = RichTextField()
    categorys = models.ForeignKey(classification,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
