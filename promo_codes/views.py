from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def validate(request):
    return JsonResponse({
        'name': 'Eduardo',
        'job': 'CodigoFacilito',
        'courses': [
            {'title': 'Python'},
            {'title': 'Java'},
            {'title': '.NET'}
        ]
    })
