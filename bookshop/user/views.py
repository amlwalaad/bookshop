from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .forms import form_signup, user_log
from .models import books , users


# Create your views here.4
def form_login(request):
    form_log = user_log()
    context = {'form_log': form_log}
    return render(request, 'user/forms_log.html', context)


def form_reg(request):
    form_register1 = form_signup()
    context = {'form_register1': form_register1}
    if request.method == 'POST':
        form_register1 = form_signup(request.POST)
        if form_register1.is_valid():
            user = form_register1.save()
            auth_login(request, user)
            return redirect(display_home)
    return render(request, 'user/forms_register.html', context)


def detailsbookview(request,book_id):
    book_details = books.objects.filter(id=book_id)
    context = {"book_details": book_details[0]}
    return render(request, 'user/detailsofbook.html',context)


def display_home(request):
    book = books.objects.all()
    context = {'books': book}
    return render(request, 'user/home.html', context)
def allstudensview(request):
    student=users()
    context={'users':users}
    return render(request , 'user/student_page.html', context)
