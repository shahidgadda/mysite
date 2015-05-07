from django import forms
from django.forms import ModelForm

class contactForm(forms.Form):
      name = forms.CharField(label='name', max_length=100)
      email = forms.EmailField(label='email')
      message = forms.CharField(widget=forms.Textarea)
