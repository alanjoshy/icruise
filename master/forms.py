from django import forms
from master.models import Cruise, Food,Hall


class Cruiseform(forms.ModelForm):
    class Meta:
        model = Cruise
        fields = ['Cruise_name', 'Cabins', 'Cabin_types', 'Capacity', 'Year_of_built', 'Price_per_individuals',
                  'Starts_from', 'Destination', 'Description', 'Image']


class Foodform(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['Food_name', 'Food_type', 'Price', 'Quantity', 'Description', 'Food_image']


class Hallform(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['Hall_name', 'Hall_type', 'Number_of_seats', 'Amount', 'Hall_Description', 'Hall_image']
