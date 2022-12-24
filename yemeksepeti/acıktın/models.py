from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)


class Restoran(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(20)])
    image_name = models.CharField(max_length=50)
    image_cover = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.models.DecimalField(max_digits=19, decimal_places=2)
    open_close = models.CharField(max_length=100)


class Person(models.Model):
    genders = (
        ("M", "Male"),
        ("F", "Female"),
    )
    duty_types = (
        ("1", "Crew")
        ("2", "Cast")
        ("3", "Director")
        ("4", "Writer")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=genders)
    duty_type = models.CharField(max_length=1, choices=duty_types)