from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def deduct(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))


def success(request, args):
    amount = args
    return render(request, 'app/success.html', {'amount': amount})
