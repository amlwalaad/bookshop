from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import form_reg, display_home, detailsbookview , allstudensview

urlpatterns = [
    path('home/<int:book_id>/', detailsbookview),
    path('allstudent/', allstudensview , name="student"),
    path('register/', form_reg, name="register"),
    path('log_in/', auth_views.LoginView.as_view(template_name="user/forms_log.html"), name="login"),
    path('home/', display_home, name='home'),

]
