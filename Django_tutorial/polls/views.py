from django.shortcuts import render

# Create your views here - changed by goofy
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Its me goofy nigaga and  You're at the poll index.")