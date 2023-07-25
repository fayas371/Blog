from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=255)
    cover=models.ImageField(blank=True,null=True,upload_to='cover/')
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    

class UserProfile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to='profile/')
    website_url=models.CharField(max_length=255,null=True,blank=True)
    facebook_url=models.CharField(max_length=255,null=True,blank=True)
    Linkedin_url=models.CharField(max_length=255,null=True,blank=True)
    Instagram_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')




class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=200)
    likes=models.ManyToManyField(User,related_name='blog_posts')
    snippet=models.CharField(max_length=100,default='The blog snipet')
    header_image=models.ImageField(null=True,blank=True,upload_to='images/')
    
    def total_likes(self):
        return self.likes.count()



    def __str__(self) -> str:
        return self.title +' | '+str(self.author)


    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
    

