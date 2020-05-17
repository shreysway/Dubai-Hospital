from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('Status', 'DoctorName', 'TokenNo', 'issues')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('Status', 'DoctorName', 'TokenNo', 'issues')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('Status', 'DoctorName', 'TokenNo', 'issues')
