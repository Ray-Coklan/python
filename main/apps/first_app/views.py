from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from ..exam_app import *
import bcrypt


def index(request):

    return render(request, 'first_app/index.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(
        first_name = request.POST['first_name'], 
        last_name = request.POST['last_name'], 
        email = request.POST['email'],
        birthday = request.POST['birthdate'],
        password = hash1,
        )
        request.session['id'] = new_user.id
        return redirect('/exam')


def login(request):
    print 'password'
    Password = request.POST['Password']
    Email = request.POST['Email']
    user = User.objects.filter(email= Email)
    if len(Password) < 1 or len(Email) < 1:
        messages.error(request,"Cannot be empty")
    if len(user) < 1:
        messages.error(request,"Email or password is incorrect")
        print 'messages.error'
        return redirect('/')
    else: 
        request.session['id'] = user[0].id
        cpassword = bcrypt.checkpw(Password.encode(), user[0].password.encode())
        if cpassword:
            print "SUCCESS"
            return redirect('/exam')
        else:
            messages.error(request,"Email or password is incorrect")
            print "PASSWORD FAILURE"
            return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')
