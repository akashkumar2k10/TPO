from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'base.html')
	
def register(request):
    if request.method == 'POST':
        gender = request.POST.get("gender")
        birth_date = request.POST.get("birth_date")
        form = SignUpForm(request.POST)
        form2 = SignUpFormProfile(request.POST)
        if form.is_valid() and form2.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email = email).exists():
                messages.warning(request, 'Username Alreay Existing')
                return redirect('register')
            form = SignUpForm(request.POST)
            context = {
            'form' : form,
            'form2' : form2,
            }
               # return render(request, 'index.html',context)
            user = form.save(commit = False)
            user.username = user.email  #username and email is same so we are not using username
            user.save()
            a = Profile.objects.filter(user = user).first()
            #a.gender = gender
            a.f_name=user.first_name
            a.l_name=user.last_name
            a.full_name = user.first_name + " " + user.last_name
            a.email=user.email
            a.birth_date = birth_date
            user.save()
            
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [a.email,]
            print(recipient_list)
            send_mail( subject, message, email_from, recipient_list )
            a.save()
            

            messages.success(request, 'Your account has succesfull created')
            return redirect('login')
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
    applied=0
    if request.method == "POST":
        profile=Profile.objects.filter(user=request.user).first()
        
        intern_id=request.POST.get("intern_Id")
        ########error intern_head=request.POST.get("intern_Head")
        if AppliedIntern.objects.filter(intern_id=intern_id ,user_id=profile.u_roll).exists():
            messages.warning(request,'You have alreay applied!')
            
            #return HttpResponse("already applied")
            applied=1
            print("***********Applied**********")
        else:
            if(profile.u_roll==None):
                messages.warning(request,'please fill the profile section!')    
                return redirect('profile') 
            obj=AppliedIntern.objects.create()
            obj.intern_id=intern_id
            obj.user_id=profile.u_roll
            #intern mail
            #subject = 'Successfully Register to'+str(intern_Head)
            #print(intern_head)
            # message = ' it  means a world to us '
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [a.email,]
            # print(recipient_list)
            # send_mail( subject, message, email_from, recipient_list )
            # ##########################
            obj.save()

            messages.success(request, 'SuccessFully Aplied')
            print("***********NOT ABLE TO APPLY**********")


    
    intern_object=Internship.objects.all()
    return render(request, 'user/internships.html',{'i':intern_object,'applied':applied})


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
            messages.success(request, 'Profile Updated!')
            return redirect('profile')
        
    else:        
        p_form=ProfileUpdateForm(instance=request.user.profile)


    form ={'p_form': p_form,}    


    return render(request, 'user/profile.html',form)

@login_required
def jobs(request):
    jobs_object = Jobs.objects.all()
    return render(request, 'user/jobs.html',{'i':jobs_object})

