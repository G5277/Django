from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse('Hello Everyone')


def say_bye(request):
    return render(request, 'bye.html', {'id': 'Gazal'})
