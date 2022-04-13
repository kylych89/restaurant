from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'