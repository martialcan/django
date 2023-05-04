from django.shortcuts import render , redirect
from .models import Food
from .forms import ReservationFormForm
from .models import ReservationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def food_list(request):
    food_list = Food.objects.all()
    context = {'foods': food_list}
    return render(request, 'foods/index.html' , context= context)
def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            Reservation.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                person=form.cleaned_data['person'],
                phone=form.cleaned_data['phone'],
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time'],
                fav=form.cleaned_data['fav'],
                occasation=form.cleaned_data['occasation']
            )
            return render(request, 'reservation_success.html')
    else:
        form = ReservationForm()
    return render(request, 'reservations.html', {'form': form})
