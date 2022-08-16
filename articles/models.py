from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User   #is the same of above code
from django.urls import reverse
# from datatime import dattime
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):   #finding the articles based on id (pk), Because the Article model contain's a primar key & id
        return reverse("article_details", kwargs={"pk": self.pk})
    


class Comment(models.Model):  #add the comment model for articles
    article=models.ForeignKey(Article, related_name='comments' , on_delete=models.CASCADE)
    comment=models.TextField()
    writer=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return str(self.writer)+"   "+ str(self.id)

    def get_absolute_url(self):
        return reverse('article_list')