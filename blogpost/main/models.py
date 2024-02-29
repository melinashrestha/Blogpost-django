from django.db import models
from django.contrib.auth.models import User

class AuthorModel(models.Model):
        name =models.CharField(max_length=128)
        email =models.EmailField()
        def __str__(self):
            return self.title
        
class CategoryModel(models.Model):
        title =models.CharField(max_length=128)
        description =models.CharField(max_length=255)
        
        def __str__(self):
            return self.title

class BlogpostModel(models.Model):
    title =models.CharField(max_length=128)
    content=models.TextField()
    # author = models.CharField(max_length=128
    image = models.ImageField(upload_to='blogpost_images/', null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at =models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.title
    
    # TODO:
    
    
   
        

        
