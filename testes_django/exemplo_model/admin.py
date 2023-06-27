from django.contrib import admin
from .models import Scan, Result


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'last_run',
        'auto_run',
    ]

    list_display_links = [
        'name',
        'last_run',

    ]

    search_fields = [
        'description',
    ]

    list_filter = [
        'last_run',
        'auto_run',
    ]

    ordering = ['name', ]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'scan',
        'bar_size',
    ]

    list_display_links = [
        'name',
        'scan',
        'bar_size',
    ]

    search_fields = [
        'description',
    ]

    list_filter = [
        'scan',
        'bar_size',
    ]

    ordering = ['name', ]
