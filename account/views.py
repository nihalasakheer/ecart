from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
      
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:        
               users = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
               users.save()
               print('user created')
               return redirect('login')
        else:
            print('password is not matching....')
            return redirect('register')
        return redirect('/')
    else:    
      return render(request, 'register.html')

def login(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         User = auth.authenticate(username=username,password=password)
         if User is not None:
             auth.login(request, User)
             return render(request, 'my_account.html')
         else:
             messages.info(request, 'invalid credential') 
             return redirect('login')   

     else:
        return render(request, 'login.html')

def my_account(request):
    return render(request, 'my_account.html')

def logout(request):
    auth.logout(request)
    return redirect('/')  
