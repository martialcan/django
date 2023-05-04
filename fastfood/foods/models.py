from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
import phonenumbers
class Food(models.Model):
    food_type = [
        ("STARTERS" , 'پیش غذا'),
        ("MAIN DISHES" , 'غذای اصلی'),
        ("DESERTS" ,'دسسر'),
        ("DEINKS" , 'نوشیدنی'),
    ]
    
    name = models.CharField(_('نام غذا') , max_length=100)
    description = models.CharField(_('توضیحات'), max_length=100)
    price = models.IntegerField(_('قیمت'), default=25000 ,  null=True)
    time = models.IntegerField(_('زمان لازم'), default=20 ,blank=True)
    photo = models.ImageField(upload_to='foods/')
    type_food = models.CharField(_("نوع غذا"),max_length=12 , choices=food_type , default="STARTERS")
   
    def __str__(self):
        return self.name
def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError('شماره صحیح نیست')
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError('Invalid phone number')

class ReservationForm(models.Model):
    prson_num = [
        ('1' , '1') ,
        ('2' , '2') ,
        ('3 ' , '3') ,
        ('4' , '4') 
   ]
    fave_food = [
        ('هندی', 'هندی'),
        ('ملی', 'ملی') ,
        ('مکزیکی', 'مکزیکی')
    ]
    oces = [
        ('عقد' , 'عقد'),
        (' تولد', 'تولد'),
        ('سالگرد','سالگرد'),
    ] 

    name = models.CharField(_('نام و نامو خانوادگی'), max_length=20)
    email = models.EmailField(_('ایمیل خود را وارد کنید'), max_length=100)
    person = models.CharField(_('تعداد افراد'), choices=prson_num, max_length=12)
    phone = models.CharField(_('شماره تلفن را وارد کنید'), max_length=11, validators=[validate_phone_number])
    date = models.DateField(_('تاریخ را وارد کنید'))
    time = models.TimeField(_('ساعت را وارد کنید'))
    fav = models.CharField(_('ترجیح غذایی'), choices=fave_food,max_length=12)
    occasation = models.CharField(_('مناسبت'), choices=oces, max_length=12)
