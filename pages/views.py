from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings


def index(request):
    return render(request, 'index.html')
