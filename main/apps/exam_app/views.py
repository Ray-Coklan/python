from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from ..first_app .models import *


def index(request):
    current_user = User.objects.get(id = request.session['id'])
    show_travel = Travel.objects.all()
    context = {
        "current_user" : current_user,
        "show_travel" : show_travel,
    }
    return render(request, 'exam_app/index.html',context)

def show_add(request, id):
    current_user = User.objects.get(id = request.session['id'])
    context = {
        "current_user" : current_user,
    }
    return render(request, 'exam_app/add.html',context)

def add(request ,id):
    current_user = User.objects.get(id = request.session['id'])
    Travel.objects.create(
        destination = request.POST['destination'],
        description = request.POST['description'],
        travel_date_from = request.POST['travel_date_from'],
        travel_date_to = request.POST['travel_date_to'],
        creator = current_user
    )
    return redirect ('/exam')

def join(request, id):
    current_user = User.objects.get(id = request.session['id'])
    join_trip = Travel.objects.get(id=id)
    join_trip.join.add(current_user)
    join_trip.save()
    print 'You have joined the trip'
    return redirect('/exam')


def show(request, id):
    show_travel = Travel.objects.get(id=id)
    user = User.objects.filter(id=id)
    context = {
        'show_travel' : show_travel,
        'user' : user
    }
    return render(request, 'exam_app/show.html', context)
