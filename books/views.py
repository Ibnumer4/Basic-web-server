from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from rest_framework import status

from .models import *
import random
# Create your views here.
@api_view(['GET'])
def homeBook(request):
    return Response( {'home': "you can select the book  by id"}  )

@api_view(['GET'])
def booklist(request):
    books = Book.objects.all()
    serializer = BookSerializer(books , many=True )
    return Response(serializer.data , status=status.HTTP_200_OK)


@api_view(['GET'])
def bookdetail(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books , many= False )
    return Response(serializer.data , status=status.HTTP_200_OK)


@api_view(['POST'])
def addBook(request):
    serializer = BookSerializer(data=request.data )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer( instance = book , data=request.data )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer( instance = book , data=request.data )
    if serializer.is_valid():
        book.delete()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_recommendations(request):
    books = Book.objects.all()
    if not books:
        return Response({'message': 'No books available for recommendations.'})
    random_book = random.choice(books)
    serializer = BookSerializer(random_book)
    return Response(serializer.data , status = status.HTTP_200_OK)






