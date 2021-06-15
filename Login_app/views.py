from Login_app.models import User
from typing import Text
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UserReg

# Create your views here.
# def home(request):
#     context_text= {
#         'text':'good to text you'
#     }
#     return render(request, 'login_app/home.html', context=context_text)

def create(request):
    if request.method == 'POST':
        fm = UserReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password= pas)
            reg.save()
            fm = UserReg()
    else:
        fm = UserReg()
    person = User.objects.all()
    return render(request, 'login_app/home.html', {'form':fm, 'blogers':person})


def update_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = UserReg(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        pi = User.objects.get(pk=id)
        form = UserReg(instance=pi)
    return render(request, 'login_app/update.html', {'form':form})


def delete_user(request, id):
    if request.method == 'POST':
        id = User.objects.get(pk=id)
        id.delete()
    return HttpResponseRedirect('/')