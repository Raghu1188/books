from django.db import models

# Create your models here.
class User(models.Model):
  Ques = models.CharField(max_length = 200)
  Answ  = models.CharField(max_length = 400)

  