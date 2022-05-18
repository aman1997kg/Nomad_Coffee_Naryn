from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

def index(request):
    base_menu = BaseMenu.objects.all()
    return render(request, 'Nomad_Coffee_Naryn_app/index.html', {"base_menu": base_menu})




