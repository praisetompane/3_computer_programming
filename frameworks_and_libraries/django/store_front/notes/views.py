from django.shortcuts import render
from django.http import HttpResponse
'''
    user added:
        views live in here
        a view is defined as f(resqust) => response
        f := request handler | action
'''

def dummy():
    y = 0
    x = 0
    a = 9
    return y

def say_hello(request):
    x = 1
    y = 2
    dummy()
    return render(request, 'hello.html', {'name': 'Bob'})
    #return HttpResponse("Hello World")