from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeBook , name='homebook'),
    path('booklist/', views.booklist , name= 'booklist'),
    path('bookdetail/', views.bookdetail , name= 'bookdetail'),

    path('addbook/', views.addBook , name= 'addbook'),
    path('updatebook/<str:pk>/', views.updateBook , name= 'updatebook'),
    path('deletebook/<str:pk>/', views.deleteBook , name= 'deletebook'),
    path('book_recommendations/', views.book_recommendations , name= 'book_recommendations'),


]
