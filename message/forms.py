from django import forms
from . import models

class CreateMessage(forms.ModelForm):
	class Meta:
		model = models.Message
		fields = ['user1','user2']