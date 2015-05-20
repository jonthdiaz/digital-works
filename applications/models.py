from django.db import models
from cms.models.fields import PlaceholderField
# Create your models here.


class Service(models.Model):
    """
        services of digital works
    """
    name = PlaceholderField('name', related_name='service_name')
    description = PlaceholderField('description',
                                   related_name='service_description')
    icon = PlaceholderField('icon', related_name='service_icon')
    status = models.BooleanField(default=False,
                                 verbose_name=u'Servicio activo')
    order = models.PositiveIntegerField(verbose_name='Orden')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')

    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Servicio'
        verbose_name_plural = u'Servicios'


class Projects(models.Model):
    """
        our projects
    """
    name = PlaceholderField('name', related_name='project_name')
    image = models.ImageField('image', upload_to='projects_images',
                              blank=True, null=True)
    description = PlaceholderField('description',
                                   related_name='project_description')
    status = models.BooleanField(default=False,
                                 verbose_name=u'Projecto activo')
    order = models.PositiveIntegerField(verbose_name='Orden')
    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=u'Fecha de creación')

    @staticmethod
    def get_important_projects():
        """
            return four projects importants
        """
        return Projects.objects.filter(status=True).order_by('order')[0:4]

    def __str__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Projecto'
        verbose_name_plural = u'Projectos'
