from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from tms.models import Users



# Create your views here.
def index(request):
    return render(request, 'login.html')


def Landingpage(request):
    return render(request, 'landing_page.html')


def Samplepage(request):
    return render(request, 'sample_page.html')

def Project_form(request):
    return render(request, 'superadmin/project_form.html')


class Project(TemplateView):
    template_name = "superadmin/project_grid.html"

