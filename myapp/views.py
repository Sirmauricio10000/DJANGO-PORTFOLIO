from django.utils import timezone
from django.shortcuts import  redirect, render
from .models import Link

# Create your views here.

def index(request):
    return render(request, "index.html")


def link_clicked(request, link_url):
    # Guardar la dirección IP y la fecha en la base de datos
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Guardar la dirección IP y la fecha en la base de datos
    Link.objects.create(ip_address=ip, date_clicked=timezone.now())

    # Realizar la redirección al enlace de GitHub
    return redirect(link_url)



