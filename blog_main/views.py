from django.shortcuts import render
from blogs.models import Blog, Category



def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True).order_by('-updated_at')
    
    context = {
        'categories' : categories,
        'featured_posts' : featured_posts,
    }
    return render(request,'home.html', context)

def search(request):
    return render(request, 'search.html')

def dashboard(request):
    return render(request, 'dashboard.html')
