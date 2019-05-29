from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')
	
def register(request):
    if request.method == 'POST':
        gender = request.POST.get("gender")
        birth_date = request.POST.get("birth_date")
        form = SignUpForm(request.POST)
        #form2 = SignUpFormProfile(request.POST)
        if form.is_valid():# and form2.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email = email).exists():
                return HttpResponse('username already exists')
                form = SignUpForm(request.POST)
                context = {
                'form' : form,
                #'form2' : form2,
                }
                print(form)
                #print(form2)
                #return render(request, 'index.html',context)
            user = form.save(commit = False)
            user.username = user.email  #username and email is same so we are not using username
            user.save()
            #a = Profile.objects.filter(user = user).first()
            #a.gender = gender
            #a.birth_date = birth_date
            #a.save()
            return HttpResponse("form saved")
    else:
        form = SignUpForm()
        #form2 = SignUpFormProfile()
    context = {
        'form' : form,
        #'form2' : form2,
    }    
    return render(request, 'index.html',context)
