from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django_countries.fields import CountryField




# Create your models here.
class Message(models.Model):
	
	# id
	messageid = models.AutoField(max_length=15,primary_key=True,unique=True)
	user1 = models.CharField(max_length=25)
	user2 = models.CharField(max_length=25)


	
	# distinction Fields
	date = models.DateTimeField(auto_now_add=True)
	messageBlock = models.TextField()
	like = models.BooleanField(default=False)
	
	
	#content


def __str__(self):
	return self.feedId

def html(self):
	return self.title