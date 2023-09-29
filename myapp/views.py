from django.utils import timezone
from django.shortcuts import  redirect, render
from .models import Link

# Create your views here.

def index(request):
    return render(request, "index.html")


def link_clicked(request, link_url):
        return redirect(link_url)



