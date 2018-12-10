from django.shortcuts import render, redirect, get_object_or_404
from Microlly.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def index(request):
	pubs = Publication.objects.all()
	return render(request, 'index.html', {'publications': pubs})

@login_required(login_url='/login')
def publication(request, title):
	pub = get_object_or_404(Publication, title=title)
	return render(request, 'publication.html', {'publication': pub})

def doLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		return  redirect('login')

def loginP(request):
		return render(request, 'connection.html')

@login_required(login_url='/login')
def log_out(request):
	logout(request)
	return redirect('/')

@login_required(login_url='/login')
def newPub(request):
	return render(request, 'newPub.html')

@login_required(login_url='/login')
def createNewPub(request):
	title = request.POST['title']
	body = request.POST['body']
	pub = Publication(title=title, body=body, user=request.user)
	pub.save()
	return redirect('publication/'+title)
	
def newUser(request):
	return render(request, 'newUser.html')

def createNewUser(request):
	p_username = request.POST['username']
	p_password = request.POST['password']
	user = User.objects.create_user(username=p_username, password=p_password)
	user.save()
	login(request, user)
	return redirect('/login')

@login_required(login_url='/login')
def deletePub(request, id):
	username = request.user.username
	print(username)
	pub = Publication.objects.get(id=id)
	if pub.user.username == username:
		print(pub.user.username)
		pub.delete()
		return redirect('/')
	else:
		return redirect('/')