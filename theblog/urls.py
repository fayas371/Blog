
from django.urls import path
from .views import *


urlpatterns =[
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_categoy/',AddCategory.as_view(),name='add-category'),
    path('edit_post/<int:pk>',EditPost.as_view(),name='edit-post'),
    path('delete_post/<int:pk>',DeletePost.as_view(),name='delete-post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('categories/',CategoryListView,name='category-list'),
    path('like/<int:pk>/',LikeView,name='like_post'),
]
