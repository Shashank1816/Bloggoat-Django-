from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    #we'll add thumbnails and other things later
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:40]+'...(and more)'
