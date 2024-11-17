from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home , name= 'home'),

    path('name/', views.name , name= 'name'),

    path('hobby/', views.hobby , name= 'hobby'),

    path('dream/', views.dream , name= 'dream'),
]



