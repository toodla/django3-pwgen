from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
        return render(request, 'generator/home.html')

def password(request):

        characters = list('abcdefghijkllmnopqrstuvwxyz')

        if request.GET.get('uppercase'):
                characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        if request.GET.get('numbers'):
                characters.extend(list('1234567890'))
        
        if request.GET.get('special'):
                characters.extend(list('$@!&*()!@'))
        
        length = int(request.GET.get('length', 12)) 
        the_password = ''
        for x in range(length):
                the_password += random.choice(characters)
        return render(request, 'generator/password.html', {'password': the_password})


def about(request):
        return render(request, 'generator/about.html')