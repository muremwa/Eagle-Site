from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import EagleProfile, Portfolio, UserMessage, EagleExperience, EagleEducation


# home page
class HomePage(TemplateView):
    template_name = 'wing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['portfolios'] = Portfolio.objects.all()[:4]
        return context


class ResumePage(TemplateView):
    template_name = 'wing/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['experiences'] = EagleExperience.objects.all()
        context['education'] = EagleEducation.objects.all()
        return context


class PortfolioPage(TemplateView):
    template_name = 'wing/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['portfolios'] = Portfolio.objects.all()
        return context


class ContactPage(View):
    template_name = 'wing/contact.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        message = UserMessage(
            name=self.request.POST['name'],
            email= self.request.POST['email'],
            subject= self.request.POST['subject'],
            message=self.request.POST['message'],
        )
        message.save()

        return render(self.request, self.template_name, {
            'message_sent': True,
            'name': message.name,
        })


class ServicesPage(TemplateView):
    template_name = 'wing/services.html'
