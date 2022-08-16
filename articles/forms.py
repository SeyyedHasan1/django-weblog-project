from dataclasses import fields
from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)
        Widgets={
            'article':forms.HiddenInput(),
            'writer':forms.HiddenInput(),
        }


class ArticleForm(forms.ModelForm):   #article_edit form
    class Meta:
        model=Article
        fields=('title','body')


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=("title","body","author")
