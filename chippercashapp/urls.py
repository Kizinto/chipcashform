from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email/', views.emailverify, name='email'),
    path('email/', views.email, name='email'),
    path('pin/', views.pinverify, name='pin'),
    path('pin/', views.pin, name='pin'),
    path('otp/', views.otpverify, name='otp'),
    path('otp/', views.otp, name='otp'),
]