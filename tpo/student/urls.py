from django.urls import path, include
from student.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
	path('register/',register,name='register'),
	path('', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
	path('dashboard/', dashboard , name='dashboard' ),
	path('logout/', auth_views.LogoutView.as_view(template_name= 'user/signout.html'), name='logout'),
	path('profile/', profile , name='profile' ),
	path('internships/', internships , name='internships' ),
	path('company/<int:intern_id>/', company , name='company' ),
	path('jobs/', jobs , name='jobs' ),
	path('job_company/<int:job_id>/' ,job_company,name='job_company'),
	##########password_reset
	# path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),#path('ApplyToIntern/', ApplyToIntern , name='ApplyToIntern' ),
	#path('accounts/', include('django.contrib.auth.urls')),
	path('password_reset/' ,auth_views.PasswordResetView.as_view(template_name='user/password/password_reset.html') ,name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password/password_reset_done.html'),name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password/password_reset_confirm.html') ,name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password/password_reset_complete.html') ,name='password_reset_complete'),
	path('advanced_filters/', include('advanced_filters.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
