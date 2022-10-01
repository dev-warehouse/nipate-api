from django.contrib import admin
from .models import ProviderModel, ProviderService


@admin.register(ProviderModel)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['UserID']


@admin.register(ProviderService)
class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ['ProviderServiceName', 'ProviderID', 'ProductID', 'LocationID']