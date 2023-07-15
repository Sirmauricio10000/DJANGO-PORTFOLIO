from threading import current_thread
from django.shortcuts import  redirect, render
from .models import Link

# Create your views here.

def index(request):
    return render(request, "index.html")


def link_clicked(request, link_url):
    # Guardar la dirección IP y la fecha en la base de datos
    ip_address = request.META.get('REMOTE_ADDR')
    Link.objects.create(ip_address=ip_address, date_clicked=current_thread)

    # Realizar la redirección al enlace de GitHub
    return redirect(link_url)



