from django.forms import ModelForm
from .models import *
from django import forms


   

class ContactForm1(ModelForm):
  class Meta:
    model = tanya1
    fields = '__all__'
    widgets = {
    'a' : forms.RadioSelect(attrs={'class': "radio"}),
	  'b' : forms.RadioSelect(attrs={'class': "radio"}),
	  'c' : forms.RadioSelect(attrs={'class': "radio"}),
	  'd' : forms.RadioSelect(attrs={'class': "radio"}),
	  'e' : forms.RadioSelect(attrs={'class': "radio"}),
    } 
  
class ContactForm2(ModelForm):
  class Meta:
    model = tanya2
    fields = '__all__'
    widgets = {
    'f' : forms.RadioSelect(attrs={'class': "radio"}),
	  'g' : forms.RadioSelect(attrs={'class': "radio"}),
	  'h' : forms.RadioSelect(attrs={'class': "radio"}),
	  'i' : forms.RadioSelect(attrs={'class': "radio"}),
	  'j' : forms.RadioSelect(attrs={'class': "radio"}),
    } 
class ContactForm3(ModelForm):
  class Meta:
    model = tanya3
    fields = '__all__'
    widgets = {
    'k' : forms.RadioSelect(attrs={'class': "radio"}),
	  'l' : forms.RadioSelect(attrs={'class': "radio"}),
	  'm' : forms.RadioSelect(attrs={'class': "radio"}),
	  'n' : forms.RadioSelect(attrs={'class': "radio"}),
	  'o' : forms.RadioSelect(attrs={'class': "radio"}),
    } 
class ContactForm4(ModelForm):
  class Meta:
    model = tanya4
    fields = '__all__'
    widgets = {
	  'p' : forms.RadioSelect(attrs={'class': "radio"}),
	  'q' : forms.RadioSelect(attrs={'class': "radio"}),
	  'r' : forms.RadioSelect(attrs={'class': "radio"}),
	  's' : forms.RadioSelect(attrs={'class': "radio"}),
	  't' : forms.RadioSelect(attrs={'class': "radio"}),
    }     
    	  

