import time
import thread
import pcap
import dpkt
import os
import re
import requests
from django.shortcuts import render
from django.http import HttpResponse
from yz import models
# Create your views here.
mac = []
user_list = [{"user":"yz","pwd":"123456"},]
def index(request):
	#if request.method == "POST":
	#print (username,password)
	#temp = {"user":username,"pwd":password}
	#user_list.append(temp)
	global user_list
	user_list = models.Victim.objects.all()
	return render(request,"index.html",{"data":user_list})
def test(request):
	#username = request.POST.get("username",None)
	#password = request.POST.get("password",None)
	#print (username,password)
	#models.Victim.objects.create(user = 'yz',pwd = 'bbd')
	#global user_list
	user_list = models.RecordUrls.objects.filter(id = 1)
	haha = models.Victim.objects.filter(id = 1)
	return render(request,"test.html",{"data":user_list,"yz":haha})
def show_url(request):
	id = request.GET.get("id",None)
	global user_list
	user_list = models.RecordUrls.objects.filter(id = id)
	mac = models.Victim.objects.filter(id = id)
	return render(request,"show_url.html",{"data":user_list,"mac":mac})
def login(request):
	username = request.POST.get("username",None)
	password = request.POST.get("password",None)
	if username == "admin" and password == "admin":
		global user_list
		user_list = models.Victim.objects.all()
		return render(request,"index.html",{"data":user_list})
	else:
		return render(request,"login.html")