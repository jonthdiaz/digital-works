from django.db import models
from cms.models.fields import PlaceholderField
# Create your models here.


class Service(models.Model):
    """
        services of digital works
    """
    icon = PlaceholderField('placeholder_icon')
    # description = PlaceholderField('placeholder_description')
    status = models.BooleanField(default=False,
                                 verbose_name=u'Servicio activo')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Servicio'
        verbose_name_plural = u'Servicios'
