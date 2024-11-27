from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home , name= 'home'),

    path('name/', views.name , name= 'name'),

    path('hobby/', views.hobby , name= 'hobby'),

    path('dream/', views.dream , name= 'dream'),
    path("test_api/",views.drftestapi,name="testapi"),
    path("check_record/<str:pk>/",views.check_record,name="check")

]



