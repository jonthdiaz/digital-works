from django.contrib import admin
from applications.models import Service, Projects, Customer
from cms.admin.placeholderadmin import (FrontendEditableAdminMixin,
                                        PlaceholderAdminMixin)

# Register your models here.


@admin.register(Service)
class ServiceAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                   admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'description', 'status',
                    'order', 'date_added']
    list_filter = ['status']
    frontend_editable_fields = ('name', 'description', 'icon', 'status')


@admin.register(Projects)
class ProjectsAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                    admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'description', 'status',
                    'order', 'date_added']
    list_filter = ['status']
    frontend_editable_fields = ('name', 'description', 'image', 'status')


@admin.register(Customer)
class ClientsAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                   admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'description', 'status',
                    'order', 'date_added']
    list_filter = ['status']
    frontend_editable_fields = ('name', 'description', 'image', 'status')
