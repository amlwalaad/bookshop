from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib import messages
from .forms import form_signup, form_borrowe, UserForm
from .models import books, borrowred_books
from books.forms import form_books
from datetime import date


# Create your views here.

def form_reg(request):
    form_register1 = form_signup()
    context = {'form': form_register1}
    if request.method == 'POST':
        form_register1 = form_signup(request.POST)
        if form_register1.is_valid():
            user = form_register1.save()
            auth_login(request, user)
            return redirect(display_home)
        else:
            messages.error(request, "Error")
            print(messages.error(request, "Error"))
    else:
        form_register1 = form_signup()
    return render(request, 'user/forms_register.html', context)


def date_return_view(request, book_id, user_id):
    form = form_borrowe()
    borrow_book = books.objects.get(id=book_id)
    borrow_book_form = form_books(instance=borrow_book)
    if request.method == 'POST':
        dateReturn = request.POST["date-return"]
        data_borrow = date.today()
        # print(data_borrow)
        data = {'user': user_id, 'book_id': book_id, 'data_return': dateReturn, 'data-borrowe': data_borrow}
        form = form_borrowe(data)
        if form.is_valid():
            avil = {'available': False, 'title': borrow_book.title, 'author': borrow_book.author,
                    'image': borrow_book.image, 'price': borrow_book.price, 'types': borrow_book.types,
                    'summary': borrow_book.summary}
            borrow_book_form = form_books(avil, instance=borrow_book)
            print(borrow_book_form.is_valid)
            borrow_book_form.save()
            form.save()
            return redirect(my_book_view, user_id)
    print(borrow_book.available)
    context = {'borrow_book': borrow_book}
    return render(request, 'user/shoppingcart.html', context)


def detailsbookview(request, book_id):
    book_details = books.objects.filter(id=book_id)
    if book_details[0].available == False:
        bor_book = borrowred_books.objects.get(book_id=book_id)
        print(bor_book.data_return)
        context = {"book_details": book_details[0], 'bor_book': bor_book}
    else:
        context = {"book_details": book_details[0]}
    return render(request, 'user/detailsofbook.html', context)


def display_home(request):
    book = books.objects.all()
    if request.method=='POST':
        book=books.objects.filter(available=False)
    context = {'books': book}
    return render(request, 'user/home.html', context)


def searchview(request):
    if request.method=='POST':
        student_id=request.POST['id']
        result = User.objects.filter(id__contains=student_id)
        # for student in students:
        #     if student_id == student.id:
        #         result = User.objects.get(id=student_id)
        # if request.method == 'POST':
        #     student_id = request.POST['search']
        #     return redirect(searchview, student_id)
        context = {"result": result}
        return render(request, 'user/search.html', context)
    else:
        result=''
        context = {"result": result}
        return render(request, 'user/search.html',context)



def allstudensview(request):
    student = User.objects.all()
    if request.method == 'POST':
        student_id = request.POST['search']
        return redirect(searchview, student_id)
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


def updatebook(request, PK):
    editBook = books.objects.get(id=PK)
    editbookform = form_books()
    editbookform = form_books(instance=editBook)
    if request.method == 'POST':
        editbookform = form_books(request.POST, request.FILES, instance=editBook)
        if editbookform.is_valid():
            editbookform.save()
            return redirect(display_home)
    context = {"addbookform": editbookform}
    return render(request, 'user/book_form.html', context)


def delete(request, PK):
    deletedbook = books.objects.get(id=PK)
    if request.method == 'POST':
        deletedbook.delete()
        return redirect(display_home)
    context = {'deletedbook': deletedbook}
    return render(request, 'user/deletebook.html', context)


def my_book_view(request, user_id):
    my_books = borrowred_books.objects.filter(user=user_id)
    if request.method == 'POST':
        book = borrowred_books.objects.get(id=request.POST['id'])
        availablee_book = books.objects.get(title=book.book_id)
        availablee_book.available = True
        availablee_book.save()
        book.delete()
        return redirect(my_book_view, user_id)
    context = {'my_books': my_books}
    return render(request, 'user/mybooks.html', context)

def editview(request):
    user_form = UserForm(instance=request.user)
    if request.method=='POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(profileview)
    context={"form": user_form}
    return render(request, 'user/edit.html',context)

def profileview(request):

    context = {"user": request.user, }
    if request.method == 'POST':
        return redirect(editview)
    return render(request, 'user/profile.html', context)



