from django.urls import path
from student.views import *
from django.contrib.auth import views as auth_views



urlpatterns=[
	path('register/',register,name='register'),
	path('', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
	path('dashboard/', dashboard , name='dashboard' ),
	path('logout/', auth_views.LogoutView.as_view(template_name= 'user/login.html'), name='logout'),
	path('profile/', profile , name='profile' ),
	path('internships/', internships , name='internships' ),
	path('jobs/', jobs , name='jobs' ),
	#path('ApplyToIntern/', ApplyToIntern , name='ApplyToIntern' ),

]