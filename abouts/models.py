from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='aboutus/')


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class WhyChoiceUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'why choice us'
        verbose_name_plural = 'why choice us'



class Chef(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')



    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chef'



