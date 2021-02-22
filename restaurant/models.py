from django.db import models


# Create your models here.
class MenuItem(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.item
