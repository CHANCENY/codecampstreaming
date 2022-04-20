from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import CoursesAvailable, CourseImages, EmailReciever



# Create your views here.


def indexpage(request):
	users = User.objects.all()
	size = 0
	for names in users:
		size = size + 1
	else:
		sizes = str(size)
		vides = CoursesAvailable.objects.all()
		videsize = 0
		for v in vides:
			videsize = videsize + 1
		else:
			sizev = str(videsize)
			vcouse =CourseImages.objects.all()
			vsize = 0
			for im in vcouse:
				vsize = vsize + 1
			else:
				csizec = str(vsize)
				return render(request,'index.html',{'usertotal':sizes,'videostotal':sizev,'avlbcorse':csizec})



def homecomingpage(request):
	users = User.objects.all()
	size = 0
	for names in users:
		size = size + 1
	else:
		sizes = str(size)
		vides = CoursesAvailable.objects.all()
		videsize = 0
		for v in vides:
			videsize = videsize + 1
		else:
			sizev = str(videsize)
			vcouse =CourseImages.objects.all()
			vsize = 0
			for im in vcouse:
				vsize = vsize + 1
			else:
				csizec = str(vsize)
				return render(request,'Home.html',{'usertotal':sizes,'videostotal':sizev,'avlbcorse':csizec})

def loginingpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password=request.POST['password']
		if username is not None and password is not None:
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				messages.info(request,'you have successfully log in {0}'.format(user.first_name))
				return redirect('login/homepage')
			else:
				return redirect('loginingpage')
		else:
			return redirect('loginingpage')
	else:
	    return render(request,'loginpage.html')


def coursevideostowatching(request):
	watchingvideo = request.GET['watch']
	allvideosaboutname =CoursesAvailable.objects.filter(couse_name= watchingvideo)
	return render(request,'Watching.html',{'videolist':allvideosaboutname})

def accountpersonal(request):
	return render(request,'Account.html')

def logout(request):
	auth.logout(request)
	manipulation(request)
	return render(request,'index.html')

def campcoderooms(request):
	coursename = request.GET['watch']
	indatabase = CoursesAvailable.objects.filter(couse_videos=coursename)
	return render(request,'Courses.html',{'room':indatabase})


def registrationpage(request):

	if request.method == 'POST':
		username = request.POST['username']
		first = request.POST['firstname']
		last = request.POST['lastname']
		email = request.POST['email']
		password = request.POST['password']
		passwordtwo =request.POST['password-1']
		if passwordtwo == password:
			if User.objects.filter(username=username).exists():
				messages.info('username already exists!')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, first_name=first, last_name=last, email=email, password=password)
				user.save()
				if user is not None:
					auth.authenticate(username=username, password=password)
					auth.login(request,user)
					return redirect("/")

		return render(request,'Loginpage.html')
	else:
		return render(request,'Register.html')

def loginfirstuser(request):
	return render(request,'Loginpage.html')


def manipulation(request):
	print('printing request')
	print(request)


def layoutpage(request):
	picture = CourseImages.objects.all()
	return render(request,'layout.html',{'cs':picture})


def functionsearchingvideos(request):
	if request.method =="GET":
		searchingfor = request.GET['search']
		firstcapital = searchingfor.capitalize()
		if searchingfor is not None:
			rooms = CoursesAvailable.objects.filter(couse_videos=firstcapital)
		return render(request,'Courses.html',{'room':rooms})


def changepage(request):
	return render(request,'Page-3.html')


def verifyingchange(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		
		user = User.objects.get(username=username)
		if user is not None:
			user.set_password(password)
			user.save()
			messages.info(request,'password changed successfully')
			return redirect("./")
		else:
			messages.info(request,'changing password failed!')
			return redirect('verifyingchange')
	else:
		return render(request,'Page-3.html')


def feedback(request):
	return render(request,'feedback.html')


def receivingmailofrequest(request):
	if request.method == 'POST':
		sendername = request.POST['name']
		senderemail=request.POST['email']
		sendermessage = request.POST['message']

		if sendername is not None and senderemail is not None and sendermessage is not None:
			print(sendername+senderemail+sendermessage)
			mesagerecieved = EmailReciever(sender_name=sendername,sender_email=senderemail,send_message=sendermessage)
			mesagerecieved.save()
			messages.info(request,'message sent')
			return redirect('/')
		else:
			messages.info(request,'message failed to send!')
			return redirect('/')
	else:
		return render(request,'Home.html')


