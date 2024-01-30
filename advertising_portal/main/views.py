from django.shortcuts import render, redirect
from .models import Offer, Opinion, Reservation
from .forms import AddOffertForm, EditOfferForm, MakeReservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http import JsonResponse
from datetime import datetime, timezone

# Create your views here.
def is_valid_queryparam(param):
    return param != '' and param is not None

def GetOffers(request):
    type = request.GET.get('type_select')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    capacity_in = request.GET.get('capacity')
    min_size = request.GET.get('min_size')
    max_size = request.GET.get('max_size')
    number_of_rooms_in = request.GET.get('number_of_rooms')
    
    qs = Offer.objects.all()
    if is_valid_queryparam(type) and type != "0":
        qs = qs.filter(offer_type = type)

    if is_valid_queryparam(min_price):
        qs = qs.filter(price__gte=min_price)
        
    if is_valid_queryparam(max_price):
        qs = qs.filter(price__lt = max_price)

    if is_valid_queryparam(min_size):
        qs = qs.filter(size__gte=min_size)
    
    if is_valid_queryparam(max_size):
        qs = qs.filter(size__lt = max_size)

    if is_valid_queryparam(capacity_in):
        qs = qs.filter(capacity = capacity_in)

    if is_valid_queryparam(number_of_rooms_in):
        qs = qs.filter(number_of_rooms = number_of_rooms_in)
    
    return render(request, 'main/main.html', {'offerts': qs})
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
    if request.method == 'GET':
        offert_in = Offer.objects.get(pk=offert_id)
        opinions = Opinion.objects.filter(offert = offert_in)
        allow_reservation = False
        if request.user.is_authenticated:
            if request.user != offert_in.user:
                allow_reservation = True 
    return render(request, 'main/offert_details.html', {'offert': offert_in, 'comments': opinions,
                'allow_reservation': allow_reservation})

def user_offert_detail(request, offert_id):
    offert = Offer.objects.get(pk=offert_id)
    return render(request, 'main/user_offert_detail.html', {'offert': offert})

def save_opinion(request):
    if request.method == 'POST':
        comment_in = request.POST['comment']
        rating_in = request.POST['rating']
        offert_id = request.POST['offert_id']
        user_in = request.user
        offert_in = Offer.objects.get(pk=offert_id)
        rating_in = int(rating_in)
        if(rating_in == 0 or comment_in == ''):
            print(rating_in)
            return JsonResponse({'bool': False})
        else:
            Opinion.objects.create(
            comment=comment_in,
            rating=rating_in,
            offert=offert_in,
            autor=user_in
            )
            now = datetime.now(timezone.utc)
            date = now.strftime("%b. %d, %Y, %H:%M %p")
            return JsonResponse({'bool':True, 'user_name': request.user.first_name, 'user_surname': request.user.last_name,
                                'date': date })
        
def make_reservation(request, offert_id):
    if request.method == 'POST':
        form = MakeReservation(request.POST)
        if form.is_valid():
            _offert = Offer.objects.get(pk=offert_id)
            _check_in = form.cleaned_data['check_in']
            _check_out = form.cleaned_data['check_out']
            _arrival_hour = form.cleaned_data['arrival_hour']
            _user_in = request.user
            Reservation.objects.create(
                check_in = _check_in,
                check_out = _check_out,
                offert = _offert,
                arrival_hour = _arrival_hour,
                guest = _user_in
            )
            messages.success(request," Reservation made succesfully!")
            return redirect("/main/user_reservations")       
    else:
        form = MakeReservation()
    return render(request, 'main/make_reservation.html', {'form': form})

def user_reservations(request):
    reservations = Reservation.objects.filter(guest = request.user)
    return render(request, 'main/user_reservations.html', {'reservations': reservations})

def client_reservations(request):
    offerts = Offer.objects.filter(user = request.user)
    client_reservations = Reservation.objects.filter(offert__in = offerts)
    all_reservations = client_reservations.exclude(is_rejected = True).count()
    waiting_reservations = client_reservations.filter(is_waiting = True).count()
    accepted_reservations = client_reservations.filter(is_accepted = True).count()
    print(accepted_reservations)
    return render(request, 'main/client_reservations.html', {'reservations' : client_reservations, 
                'all_reservations': all_reservations, 'waiting_reservations': waiting_reservations,
                'accepted_reservations': accepted_reservations})

def accept_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk = reservation_id)
    reservation.is_accepted = True
    reservation.is_waiting = False
    reservation.save()
    offerts = Offer.objects.filter(user = request.user)
    client_reservations = Reservation.objects.filter(offert__in = offerts)
    #return render(request, 'main/client_reservations.html', {'reservations' : client_reservations})
    return redirect("/main/client_reservations")

def reject_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk = reservation_id)
    reservation.is_rejected = True
    reservation.is_waiting = False
    reservation.save()
    offerts = Offer.objects.filter(user = request.user)
    client_reservations = Reservation.objects.filter(offert__in = offerts)
    #return render(request, 'main/client_reservations.html', {'reservations' : client_reservations})
    return redirect("/main/client_reservations")

def delait_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk = reservation_id)
    
    if reservation:
        reservation.delete()

    offerts = Offer.objects.filter(user = request.user)
    client_reservations = Reservation.objects.filter(offert__in = offerts)
    #return render(request, 'main/user_reservations.html', {'reservations' : client_reservations})
    return redirect("/main/user_reservations")

def contact_info_user(request, user_id):
    user = User.objects.get(pk = user_id)
    return render(request, 'main/contact_info_user.html', {'user' : user})

def contact_info_client(request, user_id):
    user = User.objects.get(pk = user_id)
    return render(request, 'main/contact_info_user.html', {'user' : user})