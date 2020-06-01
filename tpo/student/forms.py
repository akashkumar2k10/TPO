from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


# *************
# User Signup Form
# *************
class SignUpForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2',)


# *************
# Profile Signup Form
# *************
class SignUpFormProfile(forms.ModelForm):
	birth_date = forms.DateTimeField(
		widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD'},),
		)
	class Meta:
		model = Profile
		fields = ( 'birth_date', 'gender', )



class ProfileUpdateForm(forms.ModelForm):
	resume=forms.FileField()
	class Meta:
		model=Profile
		fields=(
				'f_name',                  
				'm_name',                  
				'l_name',                  
				'full_name',               
				'email',                   
				'u_roll',                
				'city'   ,                 
				'sem'    ,                 
				'gender'  ,                
				'addess'   ,               
				'birth_date',              
				'ditrict'    ,             
				'pin'         ,            
				'contact'      ,           
				'PREFRENCE_first',         
				'PREFRENCE_sec'   ,        
				'PREFRENCE_third'  ,       
				'Marks_10'          ,      
				'passing_year_10'    ,     
				'Marks_12'            ,    
				'passing_year_12'      ,   
				'Marks_Diploma'         ,  
				'addmission_year_Diploma', 
				'addmission_year_BE',
				'backlog'                   ,
				'sem_1_per'                 ,
				'sem_2_per',
				'sem_3_per'                 ,
				'sem_4_per'                 ,
				'sem_5_per'                 ,
				'sem_6_per'                 ,
				'sem_7_per'                 ,
				'aggregate_per_clg',
				'father_name'             ,
				'father_contact'          ,
				'mother_name'             ,
				'mother_contact'          ,
				'emergency_contact'       ,
				'course'                  ,
				'Enrollment_no'           ,
				'Dept'                    ,
				'resume',
		)
		

		
		