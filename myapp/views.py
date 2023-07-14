from django.shortcuts import  render
from .models import Visitor

# Create your views here.

def index(request):
    return render(request, "index.html")


def my_view(request):
    ip_address = request.META.get('REMOTE_ADDR')
    Visitor.objects.create(ip_address=ip_address)

