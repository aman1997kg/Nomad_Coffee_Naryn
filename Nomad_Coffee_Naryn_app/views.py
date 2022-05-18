from django.shortcuts import render, redirect
from .models import *


def index(request):
    base_menu = BaseMenu.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('index')
    else:
        form = ContactForm()

    contacts = {
       'form': form
     }

    return render(request, 'Nomad_Coffee_Naryn_app/index.html', {"base_menu": base_menu, "contact": contacts})

