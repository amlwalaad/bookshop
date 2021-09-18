from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import form_reg, display_home, detailsbookview, allstudensview,  addbook  ,updatebook,delete,date_return_view

urlpatterns = [
    path('home/<int:book_id>/', detailsbookview ),
    path('allstudent/', allstudensview, name="student"),
    path('register/', form_reg, name="register"),
    path('log_out/', auth_views.LogoutView.as_view(), name="logout"),
    path('log_in/', auth_views.LoginView.as_view(template_name="user/forms_log.html"), name="login"),
    path('setting/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),name="password_change_done"),
    path('setting/change_password/',auth_views.PasswordChangeView.as_view(template_name='user/change_password.html'),name="changePW"),
    path('home/', display_home, name='home'),
    path('borrowe/<str:book_title>/<str:user_name>/', date_return_view, name="date_return"),
    path('addbook/', addbook, name="addbook"),
    path('updateBook/<int:PK>/',updatebook,name='update'),
    path('deletebook/<int:PK>/', delete ,name='deletebook'),

]
