from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
# Create your models here(object):

GENDER = (
	('','select'),
	('Female','Female'),
	('Male','Male'),
)

PREFRENCE=(
	('','select'),
	('Placement','Placement'),
	('CAT','CAT'),
	('GATE','GATE'),
	('OTHER','OTHER'),
	)

SEM=(
	('','select'),
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'),
	(6,'6'),
	(7,'7'),
	(8,'8'),
)

DEP=(
	('CSE','CSE'),
	('IT','IT'),
	('EEE','EEE'),
	('EE','EE'),
	('CIVIL','CIVIL'),
	('MECH','MECH'),
	('ETC','ETC'),
	)

COURSE=(
	
)    

YN=(
	(1,'YES'),
	(0,'NO'),
)

# ------------------------------------------------------------------------------------------------
class Profile (models.Model):
	user                    = models.OneToOneField(User,verbose_name="User", on_delete=models.CASCADE,null=True)
	f_name                  = models.CharField(verbose_name="First Name",max_length=60,null=True)
	m_name                  = models.CharField(verbose_name="Middle Name",max_length=60,null=True,blank=True)
	l_name                  = models.CharField(verbose_name="Last Name",max_length=60,null=True)
	full_name               = models.CharField(verbose_name="Full Name",max_length=60,null=True)
	email                   = models.EmailField(max_length=50,null=True)
	u_roll                  = models.PositiveIntegerField(verbose_name="University Roll no.",null=True,validators=[MinValueValidator(100000000000,_('Please enter a valid Unvercity roll number')),MaxValueValidator(999999999999,_('Please enter a valid Unvercity roll number'))])
	city                    = models.CharField(verbose_name="City", max_length=50,null=True)
	sem                     = models.PositiveIntegerField(verbose_name="Semester",choices=SEM,null=True)
	gender                  = models.CharField(verbose_name="Gender", default = 'Male', max_length=50,choices = GENDER,null=True)
	addess                  = models.CharField(verbose_name="Address", max_length=50,null=True)
	birth_date              = models.DateField(("Date of birth"), default=datetime.date.today,null=True)
	ditrict                 = models.CharField(verbose_name="District",max_length=50,null=True)
	pin                     = models.PositiveIntegerField(verbose_name="Pin",null=True,validators=[MinValueValidator(100000,_('Please enter a valid 6 digit pin code')),MaxValueValidator(999999,_('Please enter a valid 6 digit pin code'))])
	contact                 = models.PositiveIntegerField(verbose_name="Contact",null=True,validators=[MinValueValidator(1000000000,_('Please enter a valid 10 digit contact number ')), MaxValueValidator(9999999999,_('Please enter a valid 10 digit contact number' ))] )
	PREFRENCE_first         = models.CharField(verbose_name="First prefrence",choices=PREFRENCE,null=True,max_length=20)
	PREFRENCE_sec           = models.CharField(verbose_name="Second prefrence",choices=PREFRENCE,null=True,max_length=20)
	PREFRENCE_third         = models.CharField(verbose_name="Third prefrence",choices=PREFRENCE,null=True,max_length=20)
	Marks_10                = models.PositiveIntegerField(verbose_name="10th Percentage",null=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	passing_year_10         = models.PositiveIntegerField(verbose_name="10th Passing Year YYYY",null=True)
	Marks_12                = models.PositiveIntegerField(verbose_name="12th Percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	passing_year_12         = models.PositiveIntegerField(verbose_name="12th passing year YYYY",null=True,blank=True)
	Marks_Diploma           = models.PositiveIntegerField(verbose_name="Diploma Percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	addmission_year_Diploma = models.PositiveIntegerField(verbose_name="Admisson year Diploma",null=True,blank=True)
	addmission_year_BE      = models.PositiveIntegerField(verbose_name="Admisson year BE",null=True)
	backlog                 = models.PositiveIntegerField(verbose_name="No. of active backlog",null=True)
	sem_1_per               = models.PositiveIntegerField(verbose_name="1st Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_2_per               = models.PositiveIntegerField(verbose_name="2nd Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_3_per               = models.PositiveIntegerField(verbose_name="3rd Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_4_per               = models.PositiveIntegerField(verbose_name="4th Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_5_per               = models.PositiveIntegerField(verbose_name="5th Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_6_per               = models.PositiveIntegerField(verbose_name="6th Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	sem_7_per               = models.PositiveIntegerField(verbose_name="7th Semester percentage",null=True,blank=True,validators=[MinValueValidator(0,_('Please enter a valid percentage')), MaxValueValidator(100,_('Please enter a valid percentage'))])
	aggregate_per_clg		=models.PositiveIntegerField(verbose_name="Aggregate percentage till now",null=True,blank=True)
	father_name             = models.CharField(verbose_name="Father Name",max_length=60,null=True)
	father_contact          = models.PositiveIntegerField(verbose_name="Father Contact",null=True,validators=[MinValueValidator(1000000000,_('Please enter a valid 10 digit contact number ')), MaxValueValidator(9999999999,_('Please enter a valid 10 digit contact number' ))] )
	mother_name             = models.CharField(verbose_name="Mother Name",max_length=60,null=True)
	mother_contact          = models.PositiveIntegerField(verbose_name="Mother Contact",null=True,validators=[MinValueValidator(1000000000,_('Please enter a valid 10 digit contact number ')), MaxValueValidator(9999999999,_('Please enter a valid 10 digit contact number' ))] )
	emergency_contact       = models.PositiveIntegerField(verbose_name="Emergency Contact",null=True,validators=[MinValueValidator(1000000000,_('Please enter a valid 10 digit contact number ')), MaxValueValidator(9999999999,_('Please enter a valid 10 digit contact number' ))] )
	course                  = models.CharField(verbose_name="Course", default = 'Male', max_length=50,choices = GENDER,null=True)
	Enrollment_no           = models.CharField(verbose_name="Enrollment no",null=True,max_length=6,validators=[RegexValidator(regex='[A-Z][A-z][0-9][0-9][0-9][0-9]',message=('Please enter correct Enrollment id'))])
	Dept                    = models.CharField(verbose_name="Department", max_length=50,choices = DEP,null=True)
	resume                  = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['pdf'],message="Please Upload in pdf format")])
	last_update             = models.DateTimeField(null=True,blank=True)
	
	def __str__(self):
		return f'{self.email}'

#   --------------------------------------------------------------------------------------------------------------  # 
def create_profile(sender, **kwargs):
	if(kwargs["created"]):
		user_profile = Profile.objects.create(user = kwargs["instance"])

post_save.connect(create_profile,sender=User)


class Internship(models.Model):
	#notice added day

	image               =models.ImageField(upload_to='media/internship',blank=True)
	company_name        = models.CharField(max_length=100,null=True)
	company_description = models.TextField(max_length=100000,null=True)
	Description			=models.TextField(max_length=100000,null=True)
	apply_before        = models.DateField(null=True,blank=True)
	Campus_date         = models.DateField(null=True,blank=True)
	Stipend             = models.PositiveIntegerField(verbose_name="Stipend",null=True,blank=True)
	Exam_Venue               = models.CharField(max_length=100,null=True,blank=True)
	Joining_location    =models.CharField(max_length=100,null=True,blank=True)
	duration            =models.CharField(max_length=100,null=True)
	Skill_set = models.TextField(max_length=10000, null=True)
	percentage_Agg_clg=models.PositiveIntegerField(verbose_name="Aggregate Percentage",null=True,blank=True)
	percentage_12       =models.PositiveIntegerField(verbose_name="Aggregate 10 Percentage",null=True,blank=True)
	percentage_10       =models.PositiveIntegerField(verbose_name="Aggregate 12 Percentage",null=True,blank=True)
	other_note			=models.TextField(max_length=100000,null=True,blank=True)
	def __str__(self):
		return f'{self.company_name}'

class Jobs(models.Model):
	#notice added day
	image               =models.ImageField(upload_to='media/job',blank=True)
	company_name        = models.CharField(max_length=100,null=True)
	company_description = models.TextField(max_length=100000,null=True)
	Description			=models.TextField(max_length=100000,null=True)
	apply_before        = models.DateField(null=True,blank=True)
	Campus_date         = models.DateField(null=True,blank=True)
	Salary              = models.PositiveIntegerField(verbose_name="Salary",null=True,blank=True)
	Exam_Venue          = models.CharField(max_length=100,null=True,blank=True)
	Joining_location    =models.CharField(max_length=100,null=True,blank=True)
	Skill_set = models.TextField(max_length=10000, null=True)
	percentage_Agg_clg=models.PositiveIntegerField(verbose_name="Aggregate Percentage",null=True,blank=True)
	percentage_12       =models.PositiveIntegerField(verbose_name="Aggregate 10 Percentage",null=True,blank=True)
	percentage_10       =models.PositiveIntegerField(verbose_name="Aggregate 12 Percentage",null=True,blank=True)
	other_note			=models.TextField(max_length=100000,null=True,blank=True)
	

	def __str__(self):
		return f'{self.company_name}'


class AppliedIntern(models.Model):

	intern_id     = models.ForeignKey(Internship,on_delete=models.CASCADE,null=True)
	user_id       = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	#result		  = models.CharField(max_length=10,null=True,blank=True,choices = YN)
	applied_date  = models.DateTimeField(null=True,blank=True)
		
	def __str__(self):
		name=str(self.intern_id)+"_"+str(self.user_id)
		return f'{name}'

class Appliedjob(models.Model):

	job_id     	  = models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True)
	user_id       = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	#result		  = models.CharField(max_length=10,null=True,blank=True,choices = YN)
	applied_date  =models.DateTimeField(null=True,blank=True)
	def __str__(self):
		name=str(self.job_id)+"_"+str(self.user_id)
		return f'{name}'


