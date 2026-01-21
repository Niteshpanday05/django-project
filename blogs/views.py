from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Blog,Category
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.

def posts_by_category(request,category_id):
    #fetch the post that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published', category=category_id)
   
    try:
         category= Category.objects.get(pk=category_id)
    except:
        # redirect to home page
        return redirect('home')
    
    # category = get_object_or_404(Category, pk=category_id)
    
    
    context = {
        'posts':posts,
        'category_id': category_id,
    }
    return render(request, 'posts_by_category.html',context)