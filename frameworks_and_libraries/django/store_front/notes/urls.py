'''
    user added:
        URL configuration for app
        urls.py is convention
            but not required
    usage:
        include in main urls.py
'''
from django.urls import path
from . import views

'''
    user added:
        define this as Django looks for this value
        constraints:
            case sensitive
            end path with '/'
'''
urlpatterns = [
    path('hello/', views.say_hello)
]