from django.db import models

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.Title

    Title = models.CharField(max_length=200)
    Price = models.FloatField()
    Discount_Price = models.FloatField()
    Category = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.CharField(max_length=200)