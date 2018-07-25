# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from .models import User

def add(request):
    return render(request, 'semi_app/index.html')

def register(request):
    if request.method == 'POST':
        people = User.objects.create(
            first_name = request.POST['f_name'],
            last_name = request.POST['l_name'],
            email = request.POST['email']
        )
    return redirect('/')

def display(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'semi_app/display.html', context)

def users(request, userid):
    context = {
        'users' : User.objects.filter(id = userid)
    }
    return render(request, 'semi_app/user.html', context)

def edit(request, userid):
    if request.method == 'GET':
        context = {'users' : User.objects.filter(id=userid)}
    return render(request, 'semi_app/edit.html', context)

def update(request):
    if request.method == 'POST':
        updateuser = User.objects.get(id=request.POST['userid'])
        updateuser.first_name = request.POST['f_name']
        updateuser.last_name = request.POST['l_name']
        updateuser.email = request.POST['email']
        updateuser.save()
    return redirect('/')

def delete(request, userid):
    updateuser = User.objects.get(id=userid)
    updateuser.delete()
    return redirect('/')
# def result(request):
#     return redirect('/')
# Create your views here.
