from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def login(request):
    form = LoginForm()
    return render(request,'login.html', {'loginform':form})

def manager(request):
    #clean the posted data
    if request.method == 'POST':
        form_data = LoginForm(request.POST)
        if form_data.is_valid():
            cleaned_form_data = form_data.cleaned_data
    #query the database

    #generate OTP and email

    #redirect to manager.html template
    return render(request, 'manager.html', {'form':cleaned_form_data})
