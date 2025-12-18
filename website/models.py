from django.db import models

# Create your models here.
class Home(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.hero_title


class Benefit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='benefits/', blank=True, null=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    benefits = models.TextField()
    image = models.ImageField(upload_to='ingredients/', blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email
