from django.shortcuts import render
from .models import *

# Create your views here.


def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'comments/index.html',context)



def PostDetail(request, id):
  post = Post.objects.get(id=id)
  context = {'post':post}

  return render(request,'comments/detail.html',context)