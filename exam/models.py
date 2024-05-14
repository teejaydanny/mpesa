from django.db import models

# Create your models here.
class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8)


    def __str__(self):
        return self.first_name