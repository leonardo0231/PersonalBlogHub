from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, "auth/register.html", {"form":form} )

@login_required(login_url='/user/login/')
def userInfo(request):
    return render(request, "auth/userInfo.html", {"user":request.user})
 
