from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    params = { 'blogs' : blogs}
    return render(request,'blog/index.html',params) 

def blogpost(request,id):
    post = BlogPost.objects.filter(post_id = id)[0]
    params = {'post':post}
    return render(request,'blog/blogpost.html',params)


