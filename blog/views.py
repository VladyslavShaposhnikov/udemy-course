from django.shortcuts import render, HttpResponse
from django.http import request

def index(request):
    return HttpResponse(render(request, 'blog/index.html'))