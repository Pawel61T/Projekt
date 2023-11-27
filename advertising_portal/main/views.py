from django.shortcuts import render
from .models import Offer
# Create your views here.
def GetOffers(request):
    offers = Offer.objects.all()
    logged = False
    username = None
    if request.user.is_authenticated:
        logged = True
        username = request.user.first_name
    return render(request, 'main.html', {'offers': offers, 'logged': logged, 'username': username})