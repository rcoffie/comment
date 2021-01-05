from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100)
  body  = models.TextField()
  date  = models.DateField(default=datetime.now)






  class Meta:
    ordering = ['-date']



  def __str__(self):
    return self.title()