from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import EagleDetails, Portfolio

# home page
class Home(TemplateView):
    template_name = 'wing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['eagle'] = EagleDetails.objects.all()[0]
        context['portfolios'] = Portfolio.objects.all()[:4]
        return context



