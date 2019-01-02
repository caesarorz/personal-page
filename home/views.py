from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, FormView, CreateView, DetailView
from django.template.loader import get_template

from .models import Jumbotron, Headings, NavBar

class HomeView(CreateView):
    # queryset = Jumbotron.objects.all()
    fields = '__all__'
    model = Jumbotron
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['jumbotron'] = Jumbotron.objects.all().filter(active=True)
        context['heading'] = Headings.objects.all().filter(active=True)
        return context
