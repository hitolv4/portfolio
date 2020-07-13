from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    picture = models.ImageField(upload_to='portfolio_app/images/',
                                height_field=None, width_field=None, max_length=None)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
