from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Work with database
    # Transfor data
    # Data pass
    # Http response/ Json response return
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")

def show_task(request):
    return HttpResponse("This is our task page")