# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render

# Home view: simple text response
def home(request):
    return HttpResponse("<h1>This is my Home Page</h1>")

# About view: renders an HTML template
def about(request):
    return render(request, 'about.html')
