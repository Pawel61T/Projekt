from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignupForm, SigninForm, EditUserProfileForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Registration successful!")
            return redirect("/user/signin")
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})

@login_required()
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
    return render(request,'user/signin.html',{'form': form})

@login_required()
def edit_user_profile(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            #login(request, user)
            messages.success(request, 'Profile updated successfully.')
    else:
        #if request.user.is_authenticated:
            form = EditUserProfileForm(instance=request.user)
       # else:
        #    messages.error(request, 'You must login to customize your profile.')
        #    return redirect('/')
    return render(request, 'user/edit_profile.html', {'form': form})

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/user/update_profile')
        else:
            messages.error(request, 'Please input correct data!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})

#def password_change_done(request):
#    return render(request, 'user/password_change_done.html')