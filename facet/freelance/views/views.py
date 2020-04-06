from django.shortcuts import render
from django.http import HttpResponse


def freelance(request):
    return HttpResponse("Freelance Index.")
