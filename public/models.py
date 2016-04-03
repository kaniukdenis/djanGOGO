# coding: utf-8

from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User

class Public(models.Model):
    head = models.CharField('Заголовок', max_length = 100)
    theme = models.CharField('Тема', max_length = 20)
    date_pub = models.DateTimeField('Дата публикации', default = datetime.datetime.now() )
    text = models.TextField('Текст публикации', max_length = 10000)
    author = models.CharField('Автор статьи', max_length = 100)
    image = models.ImageField()
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    users_likes = models.ManyToManyField(User)
    #users_dislikes = models.ManyToManyField(User, related_name = 'dislike')
    
    def __str__(self):
        return self.head

    def __unicode__(self):
        return self.head


class Comments(models.Model):
    class Meta():
        db_table = 'comments'


    comments_text = models.TextField()
    comments_public = models.ForeignKey(Public)


        
