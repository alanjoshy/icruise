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
from user.views import Userhomeview, Registrationview, Successview, LoginView, Userprofileview, Usercruisesview, \
    Uvdcruiseview, Bookcruiseview, success, Userhallview, Userhalldetview,Bookhallview,Userfoodview,Userfooddetview,Bookfoodview
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('userhome/', Userhomeview.as_view(), name='userhome'),
                  path('reg/', Registrationview.as_view(), name='reg'),
                  path('success/', Successview.as_view(), name='success'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name="home.html"), name='logout'),
                  path('userprofile/(?p<pk>[0-9]+)', Userprofileview.as_view(), name='userprofile'),
                  path('uvcruise/', Usercruisesview.as_view(), name='uvcruise'),
                  path('uvdcruise/(?p<pk>[0-9]+)', Uvdcruiseview.as_view(), name='uvdcruise'),
                  path('bookcruise/(?p<pk>[0-9]+)', Bookcruiseview.as_view(), name='bookcruise'),
                  path('bookcruise/success', success, name='bookcruise/success'),
                  path('uvhall/', Userhallview.as_view(), name='uvhall'),
                  path('uvhalldet/(?p<pk>[0-9]+)', Userhalldetview.as_view(), name='uvhalldet'),
                  path('bookhall/(?p<pk>[0-9]+)', Bookhallview.as_view(), name='bookhall'),
                  path('bookhall/success', success, name='bookhall/success'),
                  path('uvfood/', Userfoodview.as_view(), name='uvfood'),
                  path('uvfooddet/(?p<pk>[0-9]+)', Userfooddetview.as_view(), name='uvfooddet'),
                  path('bookfood/(?p<pk>[0-9]+)', Bookfoodview.as_view(), name='bookfood'),
                  path('bookfood/success1', success, name='bookfood/success1'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
