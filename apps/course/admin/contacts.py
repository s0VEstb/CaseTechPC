from django.contrib import admin
from ..models import Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('number', 'email', 'link_1', 'link_2')  # choose what to show
    search_fields = ('number', 'email')
    fields = ('number', 'email', 'link_1', 'link_2', 'link_3', 'link_4')
    readonly_fields = ()