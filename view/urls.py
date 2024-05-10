from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
]