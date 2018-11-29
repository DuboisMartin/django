from django.urls import path
from Microlly import views
app_name = "Microlly"

urlpatterns = [
	path('', views.index, name='index'),
	path('publication', views.publication, name='publication'),
	path('login', views.loginP, name='login'),
	path('doLogin', views.doLogin, name='doLogin'),
]
