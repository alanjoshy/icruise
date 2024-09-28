"""icruise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from master.views import Masterhomeview, Masteracview, Masteraclistview, Masteracupview, Masteracdeview, Masterafview, \
    Masterflist, Masterfoodupview,Masterfdeview,Masterahview,Masterhlistview,Masterhallupview,Masterhdeview,Homeview

urlpatterns = [
                  path('home/', Homeview.as_view(), name='home'),
                  path('masterhome/', Masterhomeview.as_view(), name='masterhome'),
                  path('masterac/', Masteracview.as_view(), name='masterac'),
                  path('masteraclist/', Masteraclistview.as_view(), name='masteraclist'),
                  path('masteracup/(?p<pk>[0-9]+)', Masteracupview.as_view(), name='masteracup'),
                  path('masteracde/(?p<pk>[0-9]+)', Masteracdeview.as_view(), name='masteracde'),
                  path('masteraf/', Masterafview.as_view(), name='masteraf'),
                  path('masterflist/', Masterflist.as_view(), name='masterflist'),
                  path('masterfoodup/(?p<pk>[0-9]+)', Masterfoodupview.as_view(), name='masterfoodup'),
                  path('masterfde/(?p<pk>[0-9]+)', Masterfdeview.as_view(), name='masterfde'),
                  path('masterah/', Masterahview.as_view(), name='masterah'),
                  path('masterhlist/', Masterhlistview.as_view(), name='masterhlist'),
                  path('masterhallup/(?p<pk>[0-9]+)', Masterhallupview.as_view(), name='masterhallup'),
                  path('masterhde/(?p<pk>[0-9]+)', Masterhdeview.as_view(), name='masterhde'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
