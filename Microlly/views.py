from django.shortcuts import render, redirect
from Microlly.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	pubs = Publication.objects.all()
	return render(request, 'index.html')

@login_required(login_url='/connection')
def publication(request, title):
	pub = get_object_or_404(Publication, title=title)
	return render(request, 'publication.html', {'publication': publication})

def doLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		return  redirect('loginP')

def loginP(request):
		return render(request, 'connection.html')