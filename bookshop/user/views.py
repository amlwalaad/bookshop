from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import form_signup
from books.models import books
from user.models import users
from books.forms import form_books


# Create your views here.4

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


def shoppingcartview(request, book_id):
    book_boorowe = books.objects.filter(id=book_id)
    context = {'book_boorowe': book_boorowe}
    return render(request, 'user/shoppingcart.html', context)


def detailsbookview(request, book_id):
    book_details = books.objects.filter(id=book_id)
    context = {"book_details": book_details[0]}
    book_details[0].available = False
    return render(request, 'user/detailsofbook.html', context)


def display_home(request):
    book = books.objects.all()
    context = {'books': book}
    return render(request, 'user/home.html', context)


def allstudensview(request):
    student = User.objects.all()
    context = {'student': student}
    return render(request, 'user/student_page.html', context)


def addbook(request):
    addbookform = form_books()
    if request.method == 'POST':
        addbookform = form_books(request.POST, request.FILES)
        if addbookform.is_valid():
            addbookform.save()
            return redirect(display_home)
    context = {"addbookform": addbookform}
    return render(request, 'user/book_form.html', context)


def updatebook(request , PK):
    editBook= books.objects.get(id=PK)
    editbookform = form_books()
    editbookform = form_books(instance=editBook)
    if request.method=='POST':
        editbookform =form_books(request.POST, request.FILES ,instance=editBook)
        if editbookform.is_valid():
            editbookform.save()
            return redirect(display_home)
    context = {"addbookform": editbookform}
    return render(request, 'user/book_form.html', context)

def delete(request,PK):
    deletedbook=books.objects.get(id=PK)
    if request.method=='POST':
        deletedbook.delete()
        return redirect(display_home)
    context={'deletedbook':deletedbook}
    return render(request , 'user/deletebook.html',context)

def mybooks(request):
    return render(request, 'user/shoppingcart.html')
