from django.shortcuts import render 


def index(request):
	return render(request,"index.html")


def indexii(request):
	return render(request,"indexii.html")