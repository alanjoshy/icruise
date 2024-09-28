from django.db import models


# Create your models here.
class Cruise(models.Model):
    Cruise_name = models.CharField(max_length=100)
    Cabins = models.IntegerField()
    Cabin_types = models.CharField(max_length=100)
    Capacity = models.IntegerField()
    Year_of_built = models.IntegerField()
    Price_per_individuals = models.IntegerField()
    TPrice = models.IntegerField(default=100)
    Starts_from = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)
    Description = models.TextField(max_length=500)
    Image = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        try:
            self.TPrice = self.Price_per_individuals * 100
        except TypeError:
            pass
        super().save(*args, **kwargs)


class Food(models.Model):
    Food_name = models.CharField(max_length=100)
    Food_type = models.CharField(max_length=100)
    Price = models.IntegerField()
    FPrice = models.IntegerField(default=100)
    Quantity = models.IntegerField()
    Description = models.TextField(max_length=300)
    Food_image = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        try:
            self.FPrice = self.Price * 100
        except TypeError:
            pass
        super().save(*args, **kwargs)



class Hall(models.Model):
    Hall_name = models.CharField(max_length=100)
    Hall_type = models.CharField(max_length=100)
    Number_of_seats = models.IntegerField()
    Amount = models.IntegerField()
    HPrice = models.IntegerField(default=100)
    Hall_Description = models.TextField(max_length=300)
    Hall_image = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        try:
            self.HPrice = self.Amount * 100
        except TypeError:
            pass
        super().save(*args, **kwargs)
