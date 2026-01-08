from django.shortcuts import render
from django.conf import settings




def home(request):
    return render(request, "home.html", {"google_tag":settings.GOOGLE_TAG})

def privacy(request):
    return render(request, "privacy.html")

def terms(request):
    return render(request, "terms.html")