from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100)
  # author = models.OneToOneField(User,on_delete=models.DO_NOTHING)
  author  = models.ForeignKey(User, on_delete= models.DO_NOTHING,blank=True,null=True)
  body  = models.TextField()
  created  = models.DateTimeField(auto_now_add=True,null=True,blank=True)
  update   = models.DateTimeField(auto_now_add=True,null=True,blank=True)






  class Meta:
    ordering = ['-created']



  def __str__(self):
    return self.title