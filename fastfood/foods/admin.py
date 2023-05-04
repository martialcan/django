from django.contrib import admin
from .models import Food, ReservationForm

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ReservationForm)
class ReservationFormAdmin(admin.ModelAdmin):
    list_display= ['id' , 'name']
