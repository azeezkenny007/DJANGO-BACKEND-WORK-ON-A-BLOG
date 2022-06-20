from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import Forms
# Create your views here.

def myview(request):
    print(request.method)
    print('this is my view page')
    post=Post.objects.all()
    kate={'mypost':post}
    print(post)
    return render(request,'aptech/index.html',context=kate)


def myview1(request,id):
    post=Post.objects.get(id=id)
    late={'post':post}
    print('this is my page')
    return render(request, 'aptech/post.html',context=late)

def myview2(request):
    print('this is my page')
    return render(request, 'aptech/contact.html')

def myview3(request):
    print('this is my page')
    return render(request, 'aptech/about.html')

def myview4(request,):
    form=Forms()
    late={'form':form}
    return render(request,'aptech/uniben.html',context=late)


