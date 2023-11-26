from django.shortcuts import render
from .models import Offer
# Create your views here.
def GetOffers(request):
    offers = Offer.objects.all()
    return render(request, 'main.html', {'offers': offers})