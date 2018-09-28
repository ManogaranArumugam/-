from django.core.exceptions import ImproperlyConfigured
from django.http import request, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from tms.models import ProjectDetails
from tms.models.common import Client, Projecttype
from tms.constants import TIMESHEET_CODE
from tms.forms.client_enduser_form import client_enduser
from django.utils.dateparse import parse_date


class Client_view(TemplateView):
    template_name = "superadmin/client_enduser_grid.html"

    def get_context_data(self, **kwargs):
        context = {'range': range(50)}
        return context


class Clientcreateview(CreateView):
    """Provide a way to show and handle a form in a request."""
    initial = {}
    model = Client
    form_class = client_enduser
    success_url = "client_view"
    template_name = "superadmin/client_enduser_form.html"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""

        if form_class is None:
            form_class = self.get_form_class()

        return form_class(**self.get_form_kwargs())

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        # if not self.success_url:
        #     raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        # return str(self.success_url)  # success_url may be lazy
        return reverse_lazy(self.success_url)  # success_url may be lazy

    def post(self, request, *args, **kwargs):

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        clienttype = form.data['client_type']
        create_by = 'siva'
        created_ip = '192.168.2.48'

        client_id = self.model.objects.filter(client_type=clienttype).count()
        client_id += 1
        client_code = TIMESHEET_CODE['clientcode'] + str(client_id) if clienttype == 'client' else TIMESHEET_CODE[
                                                                                                       'endusercode'] + str(
            client_id) if clienttype == 'end_user' else ''

        obj = form.save(commit=False)
        obj.client_id = form.cleaned_data['client_id'] = client_id
        obj.client_code = form.cleaned_data['client_code'] = client_code
        obj.created_by = form.cleaned_data['created_by'] = create_by
        obj.modified_by = form.cleaned_data['modified_by'] = create_by
        obj.created_ip = form.cleaned_data['created_ip'] = created_ip
        obj.modified_ip = form.cleaned_data['modified_ip'] = created_ip
        obj.client_status = form.cleaned_data['client_status'] = 0
        # obj.save()

        import pdb
        pdb.set_trace()

        return HttpResponseRedirect(self.get_success_url())


class ClientListview(ListView):
    """
      Returns a list of Timesheet client and end-user details

      """
    model = Client
    template_name = "superadmin/client_enduser_grid.html"

    def get_context_data(self, **kwargs):

        try:
            context = super(ClientListview, self).get_context_data(**kwargs)
            # listof_clients = self.model.objects.all()
            listof_clients = self.model.objects.filter(client_type='client')
            context = {'client_details': listof_clients}

        except:
            context = {'client_details': range(0)}

        return context


class EnduserListview(ListView):
    """
      Returns a list of Timesheet client and end-user details

      """
    model = Client
    template_name = "superadmin/client_enduser_grid.html"

    def get_context_data(self, **kwargs):

        try:
            context = super(EnduserListview, self).get_context_data(**kwargs)
            listof_clients = self.model.objects.filter(client_type='end_user')
            context = {'client_details': listof_clients}


        except:
            context = {'client_details': range(0)}

        return context
