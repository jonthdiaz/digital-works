from django.contrib import admin
from applications.models import Service
from cms.admin.placeholderadmin import (FrontendEditableAdminMixin,
                                        PlaceholderAdminMixin)
from cms.models.fields import PlaceholderField

# Register your models here.


@admin.register(Service)
class ServiceAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                   admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'description', 'status',
                    'date_added']
    list_filter = ['status']
    frontend_editable_fields = ('name', 'description', 'icon', 'status')
