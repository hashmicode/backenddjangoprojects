from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def nihaoPageView(request):
    return HttpResponse('nĭ hăo means Hello in Chinese')
