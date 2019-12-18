from django import forms
from . import models


class CreateUserDetail(forms.ModelForm):
	class Meta:
		model = models.user
		fields = ['username','usernameid','bio','message','DOB','sex','country','emailId']


class EditUser(forms.ModelForm):
	class Meta:
		model = models.user
		fields = ['bio','message','sex','DOB']
