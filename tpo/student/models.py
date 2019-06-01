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

SEM={
	('','select'),
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
}

# ------------------------------------------------------------------------------------------------
class Profile (models.Model):
    user            = models.OneToOneField(User,verbose_name="User", on_delete=models.CASCADE,null=True)
    name            = models.CharField(verbose_name="Name",max_length=60,null=True)
    u_roll          = models.PositiveIntegerField(verbose_name="University Roll no.",null=True)
    city            = models.CharField(verbose_name="City", max_length=50,null=True)
    sem             = models.PositiveIntegerField(verbose_name="Semesert",default=5,choices=SEM,null=True)
    gender          = models.CharField(verbose_name="Gender", default = 'Male', max_length=50,choices = GENDER,null=True)
    addess          = models.CharField(verbose_name="Address", max_length=50,null=True)
    birth_date      = models.DateField(("Date of birth"), default=datetime.date.today,null=True)
    ditrict         = models.CharField(verbose_name="District",max_length=50,null=True)
    pin             = models.PositiveIntegerField(verbose_name="Pin",null=True)
    contact         = models.PositiveIntegerField(verbose_name="Contact",null=True)
    
    def __str__(self):
        return f'{self.user.first_name}'

#   --------------------------------------------------------------------------------------------------------------  # 
def create_profile(sender, **kwargs):
    if(kwargs["created"]):
        user_profile = Profile.objects.create(user = kwargs["instance"])

post_save.connect(create_profile,sender=User)


