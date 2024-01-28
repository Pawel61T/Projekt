from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from .forms import SignupForm, SigninForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            return redirect("/user/signin")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect("/")
    
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password.')
                #return render(request,'signin.html',{'form': form})        
    else:
        form = SigninForm()    
    return render(request,'signin.html',{'form': form})