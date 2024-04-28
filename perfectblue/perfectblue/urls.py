"""
Definition of urls for perfectblue.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from perfectblue import settings 
import theapp.views 

urlpatterns = [
    path('', theapp.views.first, name='home'),
    path('about/', theapp.views.second, name='about1'),
    path('contact/', theapp.views.third, name='contact2'),
    path('products/', theapp.views.items, name='products1'),
    path('insert/<int:id>', theapp.views.cpinsert, name='insert'),
    path('pdisplay', theapp.views.ppdisplay, name='ppdisplay'),

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
