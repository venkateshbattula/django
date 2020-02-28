from django.db import models

# Create your models here.


class users(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    type_of_register = models.CharField(max_length=25)

    def __str__(self):
        return self.name + '-' + self.type_of_register

