from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import news
from .forms import RegistarationForms
from .models import RegistrationData

# Create your views here.

def home(request):

    context = {
        "greetings" : "Hello",
        "joining" : "My name is",
        "name" : "Joesh_Gichon"
    }


    return render(request, 'home.html', context)

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

'''
def newsdate(request, year):

    article_list = news.objects.filter(pub_date_year = year)

    context = {
        'year' : year,
        'article_list' : article_list
    }


    return render(request, 'newsdate.html')

'''


def contact(request):
    context = {
        "phone1": '+254 717830906',
        "phone2": '+254 797737128'
    }

    return render(request, 'contacts.html', context)


def signup(request):

    context = {
        "form":RegistarationForms
    }

    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistarationForms(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],password = form.cleaned_data['password'], email = form.cleaned_data['email'], phone = form.cleaned_data['phone'] )


        myregister.save()


    return redirect('home')








