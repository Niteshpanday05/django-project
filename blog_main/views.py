from django.shortcuts import render
from blogs.models import Category



def home(request):
    categories=Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'home.html',{'categories':categories})

def search(request):
    return render(request, 'search.html')

def dashboard(request):
    return render(request, 'dashboard.html')
