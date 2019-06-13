from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'index.html')
	
def register(request):
    if request.method == 'POST':
        gender = request.POST.get("gender")
        birth_date = request.POST.get("birth_date")
        form = SignUpForm(request.POST)
        form2 = SignUpFormProfile(request.POST)
        if form.is_valid() and form2.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email = email).exists():
                return HttpResponse('username already exists')
                form = SignUpForm(request.POST)
                context = {
                'form' : form,
                'form2' : form2,
                }
                print(form)
                print(form2)
               # return render(request, 'index.html',context)
            user = form.save(commit = False)
            user.username = user.email  #username and email is same so we are not using username
            user.save()
            a = Profile.objects.filter(user = user).first()
            a.gender = gender
            a.name = user.first_name + " " + user.last_name
            a.email=user.email
            a.birth_date = birth_date
            a.save()
            return HttpResponse("form saved")
    else:
        form = SignUpForm()
        form2 = SignUpFormProfile()
    context = {
        'form' : form,
        'form2' : form2,
    }    
    return render(request, 'user/signup.html',context)

@login_required
def dashboard(request):
    profile=Profile.objects.filter(user=request.user).first()
    arg={
        'user': request.user,
        'profile':profile,
    }


    return render(request, 'user/dashboard.html', arg )


@login_required
def internships(request):
    intern_object=Internship.objects.all()

    return render(request, 'user/internships.html',{'i':intern_object})


@login_required
def profile(request):
    print("******************************")
    print(request.user)
    print("******************************")
    if request.method=='POST':
        print("i am in")
        p_form=ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            print("******************************")
            p_form.save()
            print("******************************")
            return redirect('profile')
        
    else:        
        p_form=ProfileUpdateForm(instance=request.user.profile)


    form ={'p_form': p_form,}    


    return render(request, 'user/profile.html',form)

@login_required
def jobs(request):
    jobs_object = Jobs.objects.all()
    return render(request, 'user/jobs.html',{'i':jobs_object})
