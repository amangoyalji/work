from django.shortcuts import render 
from django.http import HttpResponse
import smtplib

def index(request):
	return render(request,"index.html")


def indexii(request):
	return render(request,"indexii.html")

def email(request):
	return render(request,"email.html")

def submitemail(request):
	if(request.method=="POST"):
		email=request.POST['email']
		msg=request.POST['psw']
		try:
			sender="amana6398@gmail.com"
			reciever="amanjitendragoyal@gmail.com"
			submitter=email
			link=str("https://www.tutorialspoint.com/django/django_sending_emails.htm")
			message2="you can access this ink only when jaimala jha will provide you the access\n"+link
			password="RJ-45Xtreme"
			message="Hi"
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender,password)
			server.sendmail(sender,reciever,message)
			server.sendmail(sender,submitter,message2)
			return HttpResponse("mail send")
		except:
			return HttpResponse("Wrong mail id")

	return render(request,"email.html")