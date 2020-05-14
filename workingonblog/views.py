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
			sender="link1jaimala@gmail.com"
			reciever="link1jaimla@gmail.com"
			submitter=email
			link=str("https://drive.google.com/open?id=12e74Ozi_Rx0MalT_LE1I35SOOIFxnRGD")
			message2="you can access this ink only when jaimala jha will provide you the access\n"+link
			password="JAI@2020"
			message="someone wants to acces your repository having email "+email
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(sender,password)
			server.sendmail(sender,sender,message)
			server.sendmail(sender,submitter,message2)
			return HttpResponse("mail send")
		except:
			return HttpResponse("Wrong mail id")

	return render(request,"email.html")