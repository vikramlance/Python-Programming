# from django.shortcuts import render

# # Create your views here.
# def index(request):
#    return render(request, "myapp/template/hello.html", {})

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")