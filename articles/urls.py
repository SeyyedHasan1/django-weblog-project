from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/edit/',views.article_edit,name='article_edit'),  #this is a primar key   #rewrite ArticleEditView url in newsite app
    path("<int:pk>",views.article_details,name='article_details'),  #this is a primar key  #rewrite ArticleDetailView url in newsite app
    path('<int:pk>/delete/',views.article_delete,name='article_delete'),  #this is a primar key
    path("new/",views.article_create,name='article_create'), 
    path("",views.article_list,name='article_list'), #rewrite ArticleListView url in newsite app

]
