from django.db import models

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(default=0, blank=False)
    condition = models.BooleanField(default=True, blank=False) # True: New , False: Used
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    
class Make(models.Model):
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    available = models.BooleanField()

    def __str__(self):
        return self.text