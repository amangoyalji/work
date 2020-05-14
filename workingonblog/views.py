from django.shortcuts import render 


def index(request):
	return render(request,"index.html")

def mydetails(request):
	return render(request,"mydetails.html")