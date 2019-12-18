from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from user import forms as user_forms
from .models import Message as messagemodel
from user.models import user as usermodel
from django.contrib.auth.decorators import login_required


# chat creater
@login_required(login_url="/user/choice")
def profile_view(request):
	
	user = request.user
	name = str(user.username)
	if request.method == 'POST' :
		print("$%32423424312")
		userdetail = usermodel.objects.get(pk=name)
		form = user_forms.EditUser(data=request.POST,instance=userdetail)
		if form.is_valid():
			form.save()

			return redirect('message:profile')

	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):

		userdetail = usermodel.objects.get(pk=name) 
		
		form = user_forms.EditUser(initial={'bio':userdetail.bio,'message':userdetail.message,'emailId':userdetail.emailId,'sex':userdetail.sex,'DOB':userdetail.DOB})

		return render(request,'profile.html',{'user':userdetail,'form':form})
		

	#	

	else:
		return redirect('user:detail')












# chat creater
@login_required(login_url="/user/choice")
def messageBlock_view(request,messageid):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):


		
		messagedetail = messagemodel.objects.get(messageid=messageid)
		if not(messagedetail.user1 == name or messagedetail.user2 == name):
			return redirect('message:warning',messageheader="warning",message="A illegal request was tried.")
		
		return render(request,'messageBlock.html',{ 'messagedetail':messagedetail })
		

	#	

	else:
		return redirect('user:detail')






def warning_view(request,messageheader,message):

	return render(request,'warning.html',{'messageheader':messageheader,'message':message})




@login_required(login_url="/user/choice")
def validator(request):
	user = request.user.username
	print(user)
	try:
		user = usermodel.objects.get(pk=user)
	except:
		return True
	else:
		return user.active




# chat creater
@login_required(login_url="/user/choice")
def animation_view(request):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):

		return render(request,'animation.html')
		

	#	

	else:
		return redirect('user:detail')

# chat creater
@login_required(login_url="/user/choice")
def chat_view(request,messageid):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):

		message = messagemodel.objects.get(pk=messageid)
		if not(message.user1 == name or message.user2 == name):
			return redirect('message:warning',messageheader="warning",message="A illegal request was tried.")


		message.messageBlock += "<h6>"+str(user)+"</h6>"+"<p >"+str(request.POST['chat'] )+"</p>"

		message.save()

		return redirect('message:detail',messageid)

		
		


	#	for user in 

	#	

	#	

	else:
		return redirect('user:detail')

# create message 
@login_required(login_url="/user/choice")
def create_view(request,user_2):
	user = request.user
	name = user.username
	messagemodel(user1=user,user2=user_2).save()

	print(messagemodel.objects.all())


	return redirect('message:message')



#message content

#
#
#$$$$$$$$$$$$$$$$$$$$$               DELTELTE                    $$$$$$$$$$$$$$$$$$$$$$$$$$
##
#
@login_required(login_url="/user/choice")
def messagecontent_view(request):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):
		
		userdetail = usermodel.objects.get(pk=name)



		blocks =[]

		#for blocked in user.blockList:
		#	blocks.append(usermodel.objects.get(pk=blocked))


		messages = []

		
		message = messagemodel.objects.get(user1__exact=name)
		messages.append(message)
		message = messagemodel.objects.get(user2__exact=name)
		messages.append(message)


		print(user)

		return render(request,'messageContent.html',{'blocks':blocks,'messages':messages,'user_main':user})

	#	for user in 

	#	

	#	

	else:

		return redirect('user:detail')

# home page
@login_required(login_url="/user/choice")
def home_view(request):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):
		


		return render(request,'home.html')

	elif(not validator(request)):

		return redirect('message:warning',messageheader="User confirmation failled.",message="Open registered email inbox and confirm your id with specified URL.")

	#	for user in 

	#	

	#	

	else:

		return redirect('user:detail')

# main message page
@login_required(login_url="/user/choice")
def message_view(request):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):
		
		userdetail = usermodel.objects.get(pk=name)


		users = list(usermodel.objects.order_by('?'))
		users.remove(userdetail)

		blocks =[]

		#for blocked in user.blockList:
		#	blocks.append(usermodel.objects.get(pk=blocked))
		messages = []
	
		messagelist = messagemodel.objects.filter(user1=userdetail.usernameid)
		for message in messagelist:
			messages.append(message)
	
		messagelist = messagemodel.objects.filter(user2=userdetail.usernameid)
		for message in messagelist:
			messages.append(message)
			
		messageusers = []

		for message in messages:
			messageusers.append(message.user1)
			messageusers.append(message.user2)
		print(messageusers)

		userlist = users.copy()

		for user in users:
			print( user.usernameid)
			if(user.usernameid in messageusers):
				userlist.remove(user)
		
		user = request.user
		print(user)
		return render(request,'messageMain.html',{'users':userlist,'blocks':blocks,'messages':messages,'user_main':user})

	else:

		return redirect('user:detail')
	if False:
		user = request.user()
		subsetSize = 100

		usertags = 0 # get tags on user

		feedlist = feedLister(usertags)
		feedlist = feedSequencer(feedlist)
		feed = feedCreator(feedlist,subsetSize)

	feed = feedmodel.objects.all().order_by('feedId')

	return render(request,'render.html',{'feedList':feed})

# view message
@login_required(login_url="/user/choice")
def messagedetail_view(request,messageid):
	user = request.user
	name = str(user.username)
	try :
		userdetail = usermodel.objects.get(pk=name)
	except :
		userdetail = False
	else:
		userdetail = True
	
	if( userdetail and validator(request) ):
		userdetail = usermodel.objects.get(pk=name)
		users = list(usermodel.objects.order_by('?'))
		users.remove(userdetail)
		blocks =[]

		#for blocked in user.blockList:
		#	blocks.append(usermodel.objects.get(pk=blocked))
		messages = []
	
		messagelist = messagemodel.objects.filter(user1=userdetail.usernameid)
		for message in messagelist:
			messages.append(message)
			print(message)
		messagelist = messagemodel.objects.filter(user2=userdetail.usernameid)
		for message in messagelist:
			messages.append(message)
			print(message)

		print (messages)



	
		messagedetail = messagemodel.objects.get(messageid=messageid)
		if not(messagedetail.user1 == name or messagedetail.user2 == name):
			return redirect('message:warning',messageheader="warning",message="A illegal request was tried.")




		print(messagedetail.user1)

		return render(request,'messageContent.html',{'messages':messages,'blocks':blocks,'messagedetail':messagedetail,'user_main':user,'messageid':messageid})

	#	for user in 

	#	

	#	

	else:

		return redirect('user:detail')
