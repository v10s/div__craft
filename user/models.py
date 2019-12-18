import uuid
from django.db import models
from multiselectfield import MultiSelectField
from django_countries.fields import CountryField
from django_mysql.models import ListCharField

sex_choices =(('Male','Male'),('Female','Female'),('Other','Other'),('Rather not ask','Rather not ask'))
profile_choices = (('Male','<img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png">'),('Female','Female'),('Other','Other'),('Rather not ask','Rather not ask'))


# Create your models here.
class user(models.Model):

	#userid = models.AutoField(default=0,primary_key=True)
	active = models.BooleanField(default=False)
	activate_pass = models.CharField(default=uuid.uuid1(),max_length=100)
	username = models.CharField(max_length=25)
	usernameid = models.CharField(default='',max_length=25,unique=True,blank=False,primary_key=True)
	#profile_pic = models.CharField(max_length=100,choices=profile_choices)
	#asssociaters
	bio = models.CharField(default='',max_length=200)
	message = models.CharField(default='',max_length=2000)

	blockList = ListCharField(default='',base_field=models.CharField(default='',max_length=25),size=10000,max_length=(100000*25))

	DOB = models.DateField(blank=False)
	sex = models.CharField(max_length=25,choices=sex_choices)
	country = CountryField(default='',blank=True)
	
	emailId = models.EmailField(max_length=64,unique=True,blank=False)


def __str__(self):
	return (self.username)