from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection,transaction
from django.contrib.auth import login,logout
from django.core.mail import send_mail
from django.contrib import messages

from operator import itemgetter

import datetime

cursor=connection.cursor()
# Create your views here.
def index(request):
	return HttpResponse("hello world")
	
def Main_page(request):
	return render(request,'bank/Main_page.html')
	
def display(request):
	return render(request,'bank/display.html')
	
def result(request):
	return render(request,'bank/result.html')
	
def onetask(request):
	ifsc = request.POST.get('ifsc')
	cursor.execute("select bank_id,branch,address,city,district,state from bank_branchesd where ifsc='%s'"%(ifsc))
	res=cursor.fetchall()
	print("lenght",len(res))
	l=[]
	for i in res:
		l.append(list(i))
	return render(request,"bank/display.html",{'res':l,'ifsc':ifsc})
	
	
def twotask(request):
	bname = request.POST.get('bname')
	city = request.POST.get('city')
	cursor.execute("select id_b from bank_banks where name='%s'"%(bname))
	res=cursor.fetchall()
	l=[]
	for i in res:
		l.append(list(i))
	
	print(res)
	print(l)
	bid=int(l[0][0])
	cursor.execute("select branch from bank_branchesd where bank_id='%d' and city='%s'"%(bid,city))
	res=cursor.fetchall()
	l=[]
	for i in res:
		l.append(list(i))
	
	return render(request,"bank/result.html",{'res':l,'bname':bname,'city':city})
