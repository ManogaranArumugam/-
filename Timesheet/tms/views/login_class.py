from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView


# from models import Users

class home_page(TemplateView):
    template_name = "login.html"


class Landing_page(TemplateView):
    template_name = "common/Landing_page.html"



class Dashboard(TemplateView):
    template_name = "superadmin/dashboard.html"


    def get_context_data(self, **kwargs):
            context = {'range': range(100)}
            return context


class logout(TemplateView):
    template_name = "login.html"
