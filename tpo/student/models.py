from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.db.models.signals import post_save

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
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
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

# ------------------------------------------------------------------------------------------------
class Profile (models.Model):
    user                    = models.OneToOneField(User,verbose_name="User", on_delete=models.CASCADE,null=False)
    f_name                  = models.CharField(verbose_name="First Name",max_length=60,null=False)
    m_name                  = models.CharField(verbose_name="Middle Name",max_length=60,null=False,blank=False)
    l_name                  = models.CharField(verbose_name="Last Name",max_length=60,null=False,blank=False)
    full_name               = models.CharField(verbose_name="Full Name",max_length=60,null=False)
    email                   = models.EmailField(max_length=50,null=False)
    u_roll                  = models.PositiveIntegerField(verbose_name="University Roll no.",null=False)
    city                    = models.CharField(verbose_name="City", max_length=50,null=False)
    sem                     = models.CharField(verbose_name="Semester",choices=SEM,null=False,max_length=1)
    gender                  = models.CharField(verbose_name="Gender", default = 'Male', max_length=50,choices = GENDER,null=False)
    addess                  = models.CharField(verbose_name="Address", max_length=50,null=False)
    birth_date              = models.DateField(("Date of birth"), default=datetime.date.today,null=False)
    ditrict                 = models.CharField(verbose_name="District",max_length=50,null=False)
    pin                     = models.PositiveIntegerField(verbose_name="Pin",null=False)
    contact                 = models.PositiveIntegerField(verbose_name="Contact",null=False)
    PREFRENCE_first         = models.CharField(verbose_name="First prefrence",choices=PREFRENCE,null=False,max_length=20)
    PREFRENCE_sec           = models.CharField(verbose_name="Second prefrence",choices=PREFRENCE,null=False,max_length=20)
    PREFRENCE_third         = models.CharField(verbose_name="Third prefrence",choices=PREFRENCE,null=False,max_length=20)
    Marks_10                = models.CharField(verbose_name="10th Percentage", max_length=50,null=False)
    passing_year_10         = models.PositiveIntegerField(verbose_name="10th Passing Year YYYY",null=False)
    Marks_12                = models.CharField(verbose_name="12th Percentage", max_length=50,null=False,blank=False)
    passing_year_12         = models.PositiveIntegerField(verbose_name="12th passing year YYYY",null=False)
    Marks_Diploma           = models.CharField(verbose_name="Diploma Percentage", max_length=50,null=False,blank=False)
    addmission_year_Diploma = models.PositiveIntegerField(verbose_name="Admisson year Diploma",null=False)
    addmission_year_Diploma = models.PositiveIntegerField(verbose_name="Admisson year BE",null=False)
    backlog                 = models.PositiveIntegerField(verbose_name="No. of active backlog",null=False)
    sem_1_per               = models.PositiveIntegerField(verbose_name="1st Semester percentage",null=False)
    sem_2_per               = models.PositiveIntegerField(verbose_name="2nd Semester percentage",null=False)
    sem_3_per               = models.PositiveIntegerField(verbose_name="3rd Semester percentage",null=False)
    sem_4_per               = models.PositiveIntegerField(verbose_name="4th Semester percentage",null=False)
    sem_5_per               = models.PositiveIntegerField(verbose_name="5th Semester percentage",null=False)
    sem_6_per               = models.PositiveIntegerField(verbose_name="6th Semester percentage",null=False)
    sem_7_per               = models.PositiveIntegerField(verbose_name="7th Semester percentage",null=False)
    father_name             = models.CharField(verbose_name="Father Name",max_length=60,null=False)
    father_contact          = models.PositiveIntegerField(verbose_name="Father Contact",null=False)
    mother_name             = models.CharField(verbose_name="Mother Name",max_length=60,null=False)
    mother_contact          = models.PositiveIntegerField(verbose_name="Mother Contact",null=False)
    emergency_contact       = models.PositiveIntegerField(verbose_name="Emergency Contact",null=False)
    course                  = models.CharField(verbose_name="Course", default = 'Male', max_length=50,choices = GENDER,null=False)
    Enrollment_no           = models.CharField(verbose_name="Enrollment no", max_length=50,null=False)
    Dept                     = models.CharField(verbose_name="Course", default = 'Male', max_length=50,choices = DEP,null=False)

    def __str__(self):
        return f'{self.user.email}'

#   --------------------------------------------------------------------------------------------------------------  # 
def create_profile(sender, **kwargs):
    if(kwargs["created"]):
        user_profile = Profile.objects.create(user = kwargs["instance"])

post_save.connect(create_profile,sender=User)


class Internship(models.Model):
    #notice added day

    head            = models.CharField(max_length=100,null=False)
    body            = models.TextField(max_length=10000,null=False)
    apply_before    = models.DateField(default=datetime.date.today,null=False,blank=False)
    Campus_date     = models.DateField(default=datetime.date.today,null=False,blank=False)
    Salary          = models.PositiveIntegerField(verbose_name="Salary",null=False,blank=False)
    Venue           = models.CharField(max_length=100,null=False,blank=False)
    Joining_location= models.CharField(max_length=100,null=False,blank=False)
    percentage_Aggregate=models.PositiveIntegerField(verbose_name="Aggregate Percentage",null=False,blank=False)
    percentage_12=models.PositiveIntegerField(verbose_name="Aggregate Percentage",null=False,blank=False)
    percentage_10=models.PositiveIntegerField(verbose_name="Aggregate Percentage",null=False,blank=False)
    experience      =models.CharField(max_length=100,)
    def __str__(self):
        return f'{self.head}'

class Jobs(models.Model):
    #notice added day
    head          = models.CharField(max_length=100,null=False)
    body          = models.CharField(max_length=500,null=False)
    starting_date = models.DateField(default=datetime.date.today,null=False)
    ending_date   = models.DateField(default=datetime.date.today,null=False)

    def __str__(self):
        return f'{self.head}'


class AppliedIntern(models.Model):

    intern_id     = models.PositiveIntegerField(null=False)
    user_id       = models.PositiveIntegerField(null=False)
        
    def __str__(self):
        name=str(self.intern_id)+"_"+str(self.user_id)
        return f'{name}'

