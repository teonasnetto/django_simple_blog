from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('<str:slug>/', views.post_detail, name='post_detail'),
    path('<str:slug>/edit/', views.post_edit, name='post_edit'),
]

handler404 = 'sitemock.core.views.error_404_view'