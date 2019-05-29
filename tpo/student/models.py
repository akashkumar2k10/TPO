from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

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
    user            = models.OneToOneField(User,verbose_name="User", on_delete=models.CASCADE)
    name            = models.CharField(verbose_name="Name",max_length=60)
    u_roll          = models.PositiveIntegerField(verbose_name="University Roll no.")
    city            = models.CharField(verbose_name="City", max_length=50)
    sem             = models.PositiveIntegerField(verbose_name="Semesert",default=5,choices=SEM)
    gender          = models.CharField(verbose_name="Gender", default = 'Male', max_length=50,choices = GENDER)
    addess          = models.CharField(verbose_name="Address", max_length=50,)
    birth_date      = models.DateField(("Date of birth"), default=datetime.date.today)
    ditrict         = models.CharField(verbose_name="District",max_length=50,)
    pin             = models.PositiveIntegerField(verbose_name="Pin")
    contact         = models.PositiveIntegerField(verbose_name="Contact")
    
    def __str__(self):
        return f'{self.user.first_name}'

#   --------------------------------------------------------------------------------------------------------------  # 
