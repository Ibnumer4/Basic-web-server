from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def home(request):
    return HttpResponse("home")

def name(request):
    return HttpResponse("Nazir Umer ")

def hobby(request):
    return JsonResponse({"favoriteHobby": "My hobby is reading books and learning new things, as it fuels my curiosity and broadens my knowledge."})

def dream(request):
    return HttpResponse("My dream is to empower learning and innovation through technology and to be valued internationally and achieve success through meaningful contributions to the world.")

@api_view(['GET', 'POST'])
def drftestapi(request):
    print(request.data)
    return Response({
      "status":f"dta received successfully {request.data.get('first_name')}"
    })
@api_view(['GET'])
def check_record(request,pk):
    return Response(
        [
            pk
        ]
    
    )