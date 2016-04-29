from django.http import HttpResponse
from django.shortcuts import render_to_response


def helloKbh(request,):
    return render_to_response("kbhs/home.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})
