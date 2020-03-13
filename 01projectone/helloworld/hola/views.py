from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    return HttpResponse('nĭ hăo means Hello in Chinese')
