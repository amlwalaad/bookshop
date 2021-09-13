from django.shortcuts import render ,redirect
from . import forms
from books.models import books
# Create your views here.
def form_reg(request):
    form_register1=forms.user_register()
    form_log=forms.user_log()
    context = {'form_register1': form_register1, 'form_log': form_log}
    # if request.method == "post":
    #     if form_register1.is_valid():
    #         form_register1.save()
    #         return redirect('display_home')
    #     else:
    #         return render(request, 'user/home.html', context)
    return render(request,'user/form_register.html',context)
def display_home(request):
    book=books.objects.all()
    context={'books':book}
    return render(request,'user/home.html',context)
