from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.form_reg),
    path('home/',views.display_home , name='home')
]