from django.shortcuts import render

# Create your views here.


def home_public(request):
    """
        render del landing del home public
    """
    return render(request, 'sections/home/home_public.html')


def landing_projects(request):
    """
        render del landing del home public
    """
    return render(request, 'sections/home/projects.html')
