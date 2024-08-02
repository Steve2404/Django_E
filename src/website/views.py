# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from website.forms import SignupForm


def home(request):
    return render(request, 'website/base.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous etes inscrit sur le Site")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})
