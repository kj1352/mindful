from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def offerings(request):
    return render(request, 'offerings.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def blog(request):
    return render(request, 'blog.html', {})