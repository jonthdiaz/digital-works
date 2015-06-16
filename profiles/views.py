from django.shortcuts import render
from applications.models import Service, Projects, Customer
from django.core.mail import mail_admins

# Create your views here.


def home_public(request):
    """
        render del landing del home public
    """
    data = {}
    try:
        data['services'] = (Service.objects.filter(status=True)
                            .order_by('order'))
        data['projects'] = Projects.get_important_projects()
        data['customer'] = (Customer.objects.filter(status=True)
                            .order_by('order'))
    except Exception as e:
        message = u'Se genero un error obteniendo servicios o projectos %s' % e
        mail_admins('Error en vista home public', message)
    return render(request, 'sections/home/home_public_1.html', data)


def landing_projects(request):
    """
        render del landing del home public
    """
    return render(request, 'sections/home/projects.html')
