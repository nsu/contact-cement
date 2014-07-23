import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def echo(request):
    print request.get_full_path()
    print request.POST
    return HttpResponse()
