from django.db import models


class Post(models.Model):
    datetime = models.DateTimeField()

    title = models.CharField(max_length=140, default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='blog/image')

    def __unicode__(self):
        return self.title
