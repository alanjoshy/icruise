from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from master.forms import Cruiseform, Foodform, Hallform
from master.models import Cruise, Food, Hall


# Create your views here.
class Homeview(TemplateView):
    template_name = 'home.html'


class Masterhomeview(TemplateView):
    template_name = 'masterhome.html'


class Masteracview(CreateView):
    template_name = 'masterac.html'
    model = Cruise
    form_class = Cruiseform
    success_url = '/master/masterhome'


class Masteraclistview(ListView):
    template_name = 'masteraclist.html'
    model = Cruise
    context_object_name = 'list'


class Masteracupview(UpdateView):
    template_name = 'masterac.html'
    model = Cruise
    fields = ['Cruise_name', 'Cabins', 'Cabin_types', 'Capacity', 'Year_of_built', 'Price_per_individuals',
              'Starts_from', 'Destination', 'Description', 'Image']
    success_url = '/master/masteraclist'


class Masteracdeview(DeleteView):
    template_name = 'delbtn.html'
    model = Cruise
    success_url = '/master/masteraclist'


class Masterafview(CreateView):
    template_name = 'masteraf.html'
    model = Food
    form_class = Foodform
    success_url = '/master/masterhome'


class Masterflist(ListView):
    template_name = 'masterflist.html'
    model = Food
    context_object_name = 'list'


class Masterfoodupview(UpdateView):
    template_name = 'masteraf.html'
    model = Food
    fields = ['Food_name', 'Food_type', 'Price', 'Quantity', 'Description', 'Food_image']
    success_url = '/master/masterflist'


class Masterfdeview(DeleteView):
    template_name = 'delbtn.html'
    model = Food
    success_url = '/master/masterflist'


class Masterahview(CreateView):
    template_name = 'masterah.html'
    model = Hall
    form_class = Hallform
    success_url = '/master/masterhome'


class Masterhlistview(ListView):
    template_name = 'masterhlist.html'
    model = Hall
    context_object_name = 'list'


class Masterhallupview(UpdateView):
    template_name = 'masterah.html'
    model = Hall
    fields = ['Hall_name', 'Hall_type', 'Number_of_seats', 'Amount', 'Hall_Description', 'Hall_image']
    success_url = '/master/masterhlist'

class Masterhdeview(DeleteView):
    template_name = 'delbtn.html'
    model = Hall
    success_url = '/master/masterhlist'