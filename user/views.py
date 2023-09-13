from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid:
      form.save()
 #     massages.succes(request, 'account created succesfully')
    
  else:
    form = UserRegistrationForm()
  return render(request, 'user/register.html', {'form' : form })

       
