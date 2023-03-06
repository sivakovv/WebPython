from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse



def index(request):
    return render(request, 'resume/homePage.html')

def resumeTvorgRu(request):
    return render(request, 'resume/homePageRu.html')

def resumeDil(request):
    return render(request, 'resume/diloveResume.html')

def resumeDilEng(request):
    return render(request, 'resume/diloveResumeENG.html')

def forms(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            email = userform.cleaned_data["Email"]
            password = userform.cleaned_data["Password"]
            return HttpResponse("<h2>Hello our client. You enter in net Bank. Your Email: {0} and Password: {1}</h2>".format(email, password))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "resume/forms.html", {"form": userform})