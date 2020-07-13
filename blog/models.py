from django.db import models
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
