from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=252)
    description = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.title

        