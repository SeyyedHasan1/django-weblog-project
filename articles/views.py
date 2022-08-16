from multiprocessing import context
from turtle import tiltangle
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import FormMixin   
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, ArticleForm, ArticleCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#rewrite the ArticleListView class in newsite app
def article_list(request):
    article=Article.objects.all
    context={'articles':article}
    return render(request,'articles/article_list.html',context)


def article_details(request,pk):
    # article=Article.objects.get(id=pk)     #can't raise a 404 error if page not found
    article=get_object_or_404(Article,id=pk)  #raise a 404 error if page not found
    form=CommentForm()                      #avoid privacy problem
    if request.method=='POST':
        form=CommentForm(request.POST)  #request.post--->apply the chenges in edit page & fill the form
        obj=form.save(commit=False)
        obj.writer=request.user
        obj.article=article
        obj.save()
        return HttpResponseRedirect(request.path_info)
    
    else:
        form=CommentForm()
    return render(request,'articles/article_details.html',{'article':article,'form':form})  #add comments form


    
def article_edit(request,pk):
    article=get_object_or_404(Article,id=pk)
    if request.user==article.author:
      
        form=ArticleForm(request.POST or None,instance=article)       #when click on edit ,last contain must be exist's-->instance
        #request.post--->apply the chenges in edit page
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/'+'articles/'+str(pk))
        # else:
        #     form=ArticleForm()   #deldete all of the changes after editing proccess
        # form=ArticleForm()
        return render(request,'articles/article_edit.html',{'form':form})
    else:
            return HttpResponseForbidden('Access in edit article is Frobidden for you')


    # def test_func(self):  #allow user to access to update Article if user is authenticated, else raise 403 Error
    #     obj=self.get_object()
    #     return obj.author==self.request.user

    
@login_required
def article_delete(request,pk):
    article=get_object_or_404(Article,id=pk)
    if request.user==article.author:
        if request.method=='POST':
            article.delete()
            return HttpResponseRedirect('/'+'articles/')

        return render(request,'articles/article_delete.html',{'article':article})
    else:
            return HttpResponseForbidden('Access in delete article is Frobidden for you')

    
@login_required   
def article_create(request):
    form=ArticleCreateForm()
    if request.method=='POST':
        form=ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+"articles/")

    return render(request,'articles/article_create.html',{'form':form})


# @login_required
# def article_create(request):
#     form=ArticleForm()
#     if request.method=='POST':
#         form=ArticleForm(request.POST)
#         if form.is_valid():
#             post_title=form.changed_data['title']
#             post_body=form.cleaned_data['body']
#             post_author=request.user
#             obj=Article(title=post_title, body=post_body, author=post_author)
#             obj.save()
#             return HttpResponseRedirect("/"+"articles/")
#     else:
#         form=ArticleForm()

#     return render(request,'articles/article_create.html',{'form':form})


# class ArticleCommentView()