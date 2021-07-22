from django.contrib import admin
from django.urls import path,include

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutuser,name='logout'),


    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),

    path('create_oder/<str:pk>/',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),

    path('user-page/',views.userpage,name='user-page'),
    path('settings/',views.usersettings,name='user-settings'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete')


]


#PasswordResetView: Prompts for email to reset password
#PasswordResetDoneView: password reset sent link
#PasswordResetConfirmView: Prompts to enter new password to set after the reset link is sent to mail
#PasswordResetCompleteView: password reset complete msg.