from django.urls import path
from movieapp import  views
#localhost:8000/movie
urlpatterns=[
     path('',views.home),
     path('detail',views.detail),
     path('info',views.info)
]