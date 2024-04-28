from django.contrib import admin
from .models import Destination
from .models import Products 
from .models import PProducts 

# Register your models here.
admin.site.register(Destination) 
admin.site.register(Products) 
admin.site.register(PProducts)