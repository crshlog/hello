from django.forms import ModelForm
from .models import *
from django import forms


   

class ContactForm1(ModelForm):
  class Meta:
    model = tanya1
    fields = '__all__'
    widgets = {
      'a' : forms.RadioSelect(),
	  'b' : forms.RadioSelect(),
	  'c' : forms.RadioSelect(),
	  'd' : forms.RadioSelect(),
	  'e' : forms.RadioSelect(),
    } 
class ContactForm2(ModelForm):
  class Meta:
    model = tanya2
    fields = '__all__'
    widgets = {
      'f' : forms.RadioSelect(),
	  'g' : forms.RadioSelect(),
	  'h' : forms.RadioSelect(),
	  'i' : forms.RadioSelect(),
	  'j' : forms.RadioSelect(),
    } 
class ContactForm3(ModelForm):
  class Meta:
    model = tanya3
    fields = '__all__'
    widgets = {
      'k' : forms.RadioSelect(),
	  'l' : forms.RadioSelect(),
	  'm' : forms.RadioSelect(),
	  'n' : forms.RadioSelect(),
	  'o' : forms.RadioSelect(),
    } 
class ContactForm4(ModelForm):
  class Meta:
    model = tanya4
    fields = '__all__'
    widgets = {
	  'p' : forms.RadioSelect(),
	  'q' : forms.RadioSelect(),
	  'r' : forms.RadioSelect(),
	  's' : forms.RadioSelect(),
	  't' : forms.RadioSelect()        
    }     
    	  

