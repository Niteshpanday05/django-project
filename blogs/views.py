from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Blog


# Create your views here.

def posts_by_category(request,category_id):
    #fetch the post that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published', category=category_id)
    context = {
        'posts':posts,
    }
    return render(request, 'posts_by_category.html',context)