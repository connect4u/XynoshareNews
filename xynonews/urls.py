from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('economy',views.economy,name='economy'),
    path('international',views.international,name='international'),
    path('news',views.news,name='news'),
    path('sports',views.sports,name='sports'),
    path('technology',views.technology,name='technology'),
    path('home',views.home,name='home'),
]
