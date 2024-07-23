from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
