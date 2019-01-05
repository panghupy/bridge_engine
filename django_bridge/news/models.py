from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
