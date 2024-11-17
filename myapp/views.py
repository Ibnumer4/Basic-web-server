from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("home")

def name(request):
    return HttpResponse("Nazir Umer ")

def hobby(request):
    return JsonResponse({"favoriteHobby": "My hobby is reading books and learning new things, as it fuels my curiosity and broadens my knowledge."})

def dream(request):
    return HttpResponse("My dream is to empower learning and innovation through technology and to be valued internationally and achieve success through meaningful contributions to the world.")