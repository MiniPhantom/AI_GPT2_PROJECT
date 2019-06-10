from django.contrib import admin
from django.urls import path
from . import views
	
urlpatterns = [
        path('bhome/', views.bhome, name='bhome'),
        path('<int:blog_id>/', views.detail, name='detail'),
        path('bnew/', views.bnew, name='bnew'),
        path('create/', views.create, name='create'),
        path('delete/<int:blog_id>/', views.delete, name='delete'),
        path('update/<int:blog_id>/', views.update, name='update'),
        path('edit/<int:blog_id>/', views.edit, name='edit'),
        
]