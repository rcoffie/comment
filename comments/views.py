from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.


def Home(request):
  posts = Post.objects.all()
  context = {'posts':posts}
  return render(request,'comments/index.html',context)



def PostDetail(request, id):
  post = Post.objects.get(id=id)
  comments = Comment.objects.filter(post=post).order_by('-id')

  if request.method == 'POST':
     content = request.POST.get('content')
     comment = Comment.objects.create(user=request.user, post=post, content=content)
     comment.save()
     return HttpResponseRedirect(reverse('detail', args=[post.id]))

  context = {'post':post,'comments':comments}

  return render(request,'comments/detail.html',context)