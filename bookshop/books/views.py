from django.shortcuts import render

# Create your views here.
def displaybooks(request):
    return render(request , 'books/detialsbooks' )