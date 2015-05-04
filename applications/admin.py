from django.contrib import admin
from applications.models import Service
from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.


class ServiceAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'icon', 'description', 'status', 'date_added']
    list_filter = ['status']


admin.site.register(Service, ServiceAdmin)
