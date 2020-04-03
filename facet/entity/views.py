from django.shortcuts import render
from django.http import HttpResponse


def entity(request):
    return HttpResponse("Entity Index.")
