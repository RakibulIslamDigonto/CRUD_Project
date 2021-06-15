from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class User(models.Model):
    name = CharField(max_length=100)
    email = EmailField()
    password = CharField(max_length=30)
    
    def __str__(self):
        return(self.name)

