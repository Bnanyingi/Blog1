from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'Aboutus.html')

def contact(request):
    return render(request, 'Contact.html')

def other(request):
    return render(request, 'Other.html')