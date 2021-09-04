from django.shortcuts import render
from django.http import HttpResponse
'''
    user added:
        views live in here
        a view is defined as f(resqust) => response
        f := request handler | action
'''


def say_hello(request):
    return HttpResponse("Hello World")