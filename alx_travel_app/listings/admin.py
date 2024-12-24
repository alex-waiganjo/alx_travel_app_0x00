from django import forms
from django.contrib import admin
from .models import Listing,Review,Booking
from django.forms import DateInput
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget


class BookingAdmin(admin.ModelAdmin):
    
    list_display= ('booking_id','listing_id','user_id','start_date','end_date','total_price','status','created_at')
    list_filter = ('created_at',)
    search_fields = ('status',)

    formfield_overrides = {
        models.DateField: {'widget': AdminDateWidget},
    }

admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(Booking,BookingAdmin)
