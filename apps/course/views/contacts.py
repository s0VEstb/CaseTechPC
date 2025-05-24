from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.contacts import Contacts
from django.shortcuts import render
from django.http import HttpResponseBadRequest


def contacts_view(request):
    if request.method == 'GET':
        contacts = Contacts.objects.first()  
        return render(request, 'contacts.html', {
            'contacts': contacts,
        })
    else: 
        return HttpResponseBadRequest({
            'error': 'Invalid request method. Please use GET.',
        })

