from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model  = Volunteer
        fields = ['name', 'email', 'phone', 'skill', 'city', 'is_active']
        widgets = {
            'name'  : forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Full name'}),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email address'}),
            'phone' : forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Phone number'}),
            'skill' : forms.Select(attrs={
                'class': 'form-select'}),
            'city'  : forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'City'}),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
        }