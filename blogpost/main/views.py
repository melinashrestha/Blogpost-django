from django.shortcuts import render
from .models import BlogpostModel,CategoryModel

def home(request):
    blogpost_objs=BlogpostModel.objects.all()
    context= {
        "blogpost":blogpost_objs
    }
    
    return render(request,'home.html',context)


def category(request):
    category_objs = BlogpostModel.objects.filter(category='')
    context={}
    return render(request, 'category.html', context)