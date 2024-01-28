from django.shortcuts import render, redirect
from .models import Offer
from .forms import AddOffertForm, EditOfferForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User

# Create your views here.
def GetOffers(request):
    offerts = Offer.objects.all()
    return render(request, 'main/main.html', {'offerts': offerts})
    #return render(request, 'main.html', {'offers': offers, 'logged': logged, 'username': username})

@login_required()
def get_user_offerts(request):
    current_user = request.user
    offerts = Offer.objects.filter(user = current_user)
    return render(request, 'main/user_offerts.html', {'offerts': offerts})

@login_required()
def add_offert(request):
    if request.method == 'POST':
        form = AddOffertForm(request.POST, request.FILES)
        if form.is_valid():
            offert = form.save(commit=False)
            offert.user = request.user
            offert.save()
            messages.success(request," Offert added succesfully!")
            return redirect("/main/user_offerts")       
    else:
        form = AddOffertForm()    
    return render(request,'main/add_offert.html',{'form': form})

@login_required()
def edit_offert(request, offert_id):
    offert = Offer.objects.get(pk=offert_id)
    if request.method == 'POST':
        form = EditOfferForm(request.POST or None, request.FILES or None, instance=offert)
        if form.is_valid():
            form.save()
            messages.success(request," Offert updatet succesfully!")
            return redirect("/main/user_offerts")   
    else:
        form = EditOfferForm(instance=offert)
    return render(request, 'main/edit_offert.html', {'form': form})

@login_required()
def delete_offert(request, offert_id):
    offert = Offer.objects.get(pk=offert_id)
    if offert:
        offert.delete()
    return redirect("/main/user_offerts")

def offert_details(request, offert_id):
    offert = Offer.objects.get(pk=offert_id)
    if(offert.user_id):
        user = User.objects.get(id=offert.user_id)
    return render(request, 'main/offert_details.html', {'offert': offert, 'user': user})

def user_offert_detail(request, offert_id):
    offert = Offer.objects.get(pk=offert_id)
    return render(request, 'main/user_offert_detail.html', {'offert': offert})