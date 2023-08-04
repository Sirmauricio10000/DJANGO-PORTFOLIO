from django.utils import timezone
from django.shortcuts import  redirect, render
from .models import Link

# Create your views here.

def index(request):
    return render(request, "index.html")


def link_clicked(request, link_url):

    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        Link.objects.create(ip_address=ip, date_clicked=timezone.now())
    finally:
        return redirect(link_url)



