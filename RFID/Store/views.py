from django.db.models.fields import EmailField
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Object
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def HomePage(request):
    object = Object.objects.all()
    context = {'object':object}
    return render(request, 'store/home.html', context)

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('home-page')

    return render(request, 'store/register.html') 

#def Edit    
