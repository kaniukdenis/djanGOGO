from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    publication_date = models.DateTimeField()
    image = models.ImageField()

    def __unicode__(self):
        return self.title
