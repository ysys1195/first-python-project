from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'myapp/index.html'
