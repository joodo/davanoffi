from django.db import models

class Post(models.Model):
    datetime = models.DateTimeField()
    
    POST_TYPES = (
        ('TXT', 'Text'),
        ('IMG', 'Image'),
        ('VOI', 'Voice'),
    )
    post_type = models.CharField(max_length=3, choices=POST_TYPES, default='TXT')
    AUTHORS = (
        ('XU', 'friend'),
        ('JO', 'just'),
    )
    author = models.CharField(max_length=2, choices=AUTHORS, default='XU')
    title = models.CharField(max_length=140, default='')

    def __str__(self):
        return self.title + ' post by ' + self.author

class ContentText(models.Model):
    post = models.OneToOneField(Post, limit_choices_to={'post_type': 'TXT'})
    content = models.TextField(default='')
    def __str__(self):
        return self.post.title
    
class ContentImage(models.Model):
    post = models.OneToOneField(Post, limit_choices_to={'post_type': 'IMG'})
    content = models.ImageField(upload_to='blog/image')
    def __str__(self):
        return self.post.title

class ContentVoice(models.Model):
    post = models.OneToOneField(Post, limit_choices_to={'post_type': 'VOI'})
    content = models.FileField(upload_to='blog/voice')
    def __str__(self):
        return self.post.title
