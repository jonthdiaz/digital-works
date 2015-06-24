from applications.forms import ContactForm
from django_decorators.decorators import json_response, requires_post
# Create your views here.


@json_response
@requires_post
def create_contact(request):
    """
        Guarda información de contacto
        retorna success and error
    """
    data = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form and form.is_valid():
            form.save()
            data['success'] = True
        else:
            data['error'] = u'%s' % form.errors.as_text()
            data['success'] = False

    return data
