from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if (request.method =='POST'):
        f = RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('blog-home')
    else:
        f = RegistrationForm()
        
    return render(request, 'users/register.html', {'form':f})
        
        
        
        
        
        
        
        
        
        # form = RegistrationForm(request.POST)
        # if (form.is_valid()):
        #     form.save()
        # else:
        #     form = RegistrationForm()
        # context = {'form':form}
        # return render(request, 'users/register.html', context)    