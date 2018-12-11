from django.urls import path
from Microlly import views
app_name = "Microlly"

urlpatterns = [
	path('', views.index, name='index'),
	path('publication/<int:id>', views.publication, name='publication'),
	path('login', views.loginP, name='login'),
	path('doLogin', views.doLogin, name='doLogin'),
	path('logout', views.log_out, name='logout'),
	path('newPub', views.newPub, name="newPub"),
	path('createNewPub', views.createNewPub),
	path('newUser', views.newUser, name="newUser"),
	path('createNewUser', views.createNewUser),
	path('deletePub/<int:id>', views.deletePub),
	path('modifyPub/<int:id>', views.modifyPub),
	path('doModifyPub/<int:id>', views.doModifyPub)
]
