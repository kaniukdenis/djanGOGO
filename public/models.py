from django.db import models
import datetime

class Public(models.Model):
    head = models.CharField('Заголовок', max_length = 100)
    theme = models.CharField('Тема', max_length = 20)
    date_pub = models.DateTimeField('Дата публикации', default = datetime.datetime.now() )
    text = models.TextField('Текст публикации', max_length = 10000)
    author = models.CharField('Автор статьи', max_length = 100)
    image = models.ImageField(blank=True)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    def __str__(self):
        return self.head


class Comments(models.Model):
    class Meta():
        db_table = 'comments'


    comments_text = models.TextField()
    comments_public = models.ForeignKey(Public)


        
