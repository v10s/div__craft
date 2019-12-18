from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import user as user_detail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User as userprim
from django.core.mail import EmailMessage

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import uuid

# feed back page
def aboutUs_view(request):

	return render(request,'aboutUs.html')



# forgot password confirmation
def forgotConfirm_view(request):
	if(request.POST):
		try:
			userDetail = user_detail.objects.get(emailId=request.POST['emailId'])
		except:
			return HttpResponse("No user registerd with given address")


		userDetail = user_detail.objects.get(emailId=request.POST['emailId'])
		# email does not exisr logic

		userDetail.activate_pass = uuid.uuid1()
		userDetail.save()

		current_site = get_current_site(request)

		mail_subject = "Forgot password"

		message = render_to_string('forgot.html',{'user':userDetail,'domain':current_site.domain,'activate_pass':userDetail.activate_pass,'user':userDetail.usernameid})

		send_mail(mail_subject,message,'divcraft45@gmail.com',[userDetail.emailId],fail_silently=False)



		return HttpResponse(" Check your Email for reset link .")


	else:
		return render(request,'forgot_form.html')


# new password creator
def newpass_view(request,activate_pass,user):
	try:
		user = userprim.objects.get(username=user)
	except:
		return redirect('message:warning',messageheader="User confirmation failled.",message="You did something wrong. Generate the link again .")

	userDetail = user_detail.objects.get(pk=user.username)

	if(userDetail.activate_pass != activate_pass):
		return redirect('message:warning',messageheader="User confirmation failled.",message="You did something wrong. Generate the link again .")


	print(user.password)
	if (request.POST):

		user.password = make_password(request.POST['password'],salt=None,hasher='default')
		userDetail.activate_pass = " "
		user.save()

		return HttpResponse("password reset successfull")
	else:

		form = PasswordChangeForm(user=user)
		return render(request,'newpass.html',{'activate_pass':activate_pass,'form':form,'user':user.username})





# create user details
def userDetail_view(request):
	userprim = request.user
	print(userprim)
	user = request.user.username
	if request.method == 'POST':
		detail_form = forms.CreateUserDetail(request.POST,request.FILES)
		if detail_form.is_valid():
			instance = detail_form.save()
			print("$$ user active status $$")
			current_site = get_current_site(request)
			mail_subject = "Acivate email."
			userDetail = user_detail.objects.get(pk=user)

			message = render_to_string('acc_active_email.html', {'user': userprim, 'domain': current_site.domain,'activate_pass':userDetail.activate_pass,})

			send_mail(mail_subject , message ,'divcraft45@gmail.com',[request.POST['emailId']] , fail_silently=False ,)

			return redirect('message:home')
	else:
		detail_form = forms.CreateUserDetail()
	return render(request,'userDetail.html',{'form':detail_form,'user':user})


def activate(request, activate_pass):
	user = request.user
	username = user.username
	userDetail = user_detail.objects.get(pk=username)

	if (userDetail.activate_pass == activate_pass):
		userDetail.active = True
		userDetail.activate_pass = ""
		userDetail.save()
		return HttpResponse("Validated")
	else:
		return HttpResponse("In Valid get new validation link")
	#try:
	#	uid = force_text(urlsafe_base64_decode(uidb64))
	#	user = user_detail.objects.get(pk=username)
	#except(TypeError, ValueError, OverflowError, User.DoesNotExist):
	#	user = None
	#if user is not None and account_activation_token.check_token(user, token):
	#	user.active = True
	#	user.save()
	#	login(request, user)
	#	return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	#else:
	#	return HttpResponse('Activation link is invalid!')

#  login a user
def login_view(request):
	if request.method == 'POST' :
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)

			return redirect('message:home')

			# redirect to source page 
			# may be not needed if kept at on first place
			# or design a closed app

	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})

# logout a user
def logout_view(request):
	logout(request)
	return redirect('message:message')

# shows the choice page
def choice_view(request):
	return render(request,'choice.html')

# Create your views here.
def registration_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('message:home')
			# lead to extra detail addition or verification
	else:
		form = UserCreationForm()

	return render(request,'regist.html',{'form':form})
