from django.shortcuts import render
from applications.models import Service

# Create your views here.


def home_public(request):
    """
        render del landing del home public
    """
    data = {}
    data['services'] = Service.objects.all()
    return render(request, 'sections/home/home_public.html', data)


def landing_projects(request):
    """
        render del landing del home public
    """
    return render(request, 'sections/home/projects.html')
