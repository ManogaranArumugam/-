from django.core.exceptions import ImproperlyConfigured
from django.http import request, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from tms.models import ProjectDetails
from tms.models import Client
from tms.forms.project_form import Projecttimesheetform
from tms.forms.sub_project_form import Subprojecttimesheetform
from django.utils.dateparse import parse_date


class Project_view(TemplateView):
    template_name = "superadmin/project_grid.html"

    def get_context_data(self, **kwargs):
        context = {'range': range(50)}
        return context


class Project_form(TemplateView):
    template_name = "superadmin/project_form.html"


class Sub_Project_form(TemplateView):
    template_name = "superadmin/sub_project_form.html"


class Sub_Project_grid(TemplateView):
    template_name = "superadmin/sub_project_grid.html"

    def get_context_data(self, **kwargs):
        context = {'range': range(5)}
        return context


class Projectcreateview(CreateView):
    """Provide a way to show and handle a form in a request."""
    initial = {}
    model = ProjectDetails
    form_class = Projecttimesheetform
    success_url = "tms:project_view"
    template_name = "superadmin/project_form.html"

    def get_initial(self):
        super(Projectcreateview, self).get_initial()

        client = [(t.id, t.client_type) for t in Client.objects.filter(client_type='client')]
        enduser = Client.objects.filter(client_type='end_user')
        self.initial = {"client_info": client, "enduser": enduser}
        return self.initial

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
        return reverse_lazy('project_view')  # success_url may be lazy

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            print('form valid')
            # import pdb
            # pdb.set_trace()
            return self.form_valid(form)
        else:
            print('form invalid')
            # import pdb
            # pdb.set_trace()
            return self.form_invalid(form)

    #
    # def form_invalid(self, form):
    #     # import pdb
    #     # pdb.set_trace()

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        project_year = form.cleaned_data['project_startdate'].year
        project_type = form.cleaned_data['project_type']
        created_by = "admin"
        created_ip = "192.168.2.14"
        project_id = self.model.objects.filter(project_year=project_year, project_type=project_type).count()
        project_id += 1

        # import pdb
        # pdb.set_trace()
        obj = form.save(commit=False)
        obj.project_id = form.cleaned_data['project_id'] = project_id
        obj.project_year = form.cleaned_data['project_year'] = project_year
        obj.created_by = form.cleaned_data['created_by'] = created_by
        obj.created_ip = form.cleaned_data['created_ip'] = created_ip
        obj.modified_by = form.cleaned_data['modified_by'] = created_by

        obj.save()
        print(form.data)

        # import pdb
        # pdb.set_trace()

        return HttpResponseRedirect(self.get_success_url())


class Projectlistview(ListView):
    """
      Returns a list of Timesheet client and end-user details

      """
    model = ProjectDetails
    template_name = "superadmin/project_grid.html"

    def get_context_data(self, **kwargs):

        try:
            context = super(Projectlistview, self).get_context_data(**kwargs)

            # listof_project = self.model.objects.all()
            listof_project = self.model.objects.filter(parent__isnull=True)

            context = {'project_details': listof_project}

        except:
            context = {'project_details': range(0)}

        return context


class Subprojectcreateview(CreateView):
    """Provide a way to show and handle a form in a request."""
    initial = {}
    model = ProjectDetails
    form_class = Subprojecttimesheetform
    success_url = "superadmin/project_grid.html"
    template_name = "superadmin/sub_project_form.html"

    def get_initial(self):
        initials = super(Subprojectcreateview, self).get_initial()
        project_pk = self.kwargs['project_id']
        projectcount = self.model.objects.filter(parent_id=project_pk).count()
        project = self.model.objects.filter(id=project_pk).get().project_code
        projectcount += 1
        sub_project_code = project + "-" + str(projectcount)
        self.initial = {"subproject_code": sub_project_code, "parent": project_pk}

        return self.initial

    def dispatch(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        self.product = get_object_or_404(ProjectDetails, pk=project_id)
        return super(
            Subprojectcreateview, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        # if not self.success_url:
        #     raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        # return str(self.success_url)  # success_url may be lazy
        return reverse_lazy('project_view')  # success_url may be lazy

    def get(self, request, *args, **kwargs):
        project_details = ProjectDetails.objects.get(
            id=int(self.kwargs['project_id'])
        )

        project_id = project_details.project_code
        kwargs.update({'project_id': project_id})
        return super(Subprojectcreateview, self).get(request, *args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Subprojectcreateview, self).get_form_kwargs(**kwargs)
        project_details = ProjectDetails.objects.get(
            id=int(self.kwargs['project_id'])
        )

        if hasattr(self, 'object'):
            kwargs.update({
                'instance': project_details,

            })
            # import pdb
            # pdb.set_trace()
        return kwargs

    def get_form_class(self):
        """Return the form class to use."""
        return self.form_class

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""

        if form_class is None:
            form_class = self.get_form_class()
            # import pdb
            # pdb.set_trace()

        return form_class(**self.get_form_kwargs())

    def post(self, request, *args, **kwargs):

        form = self.get_form()

        if form.is_valid():
            print('form valid')
            return self.form_valid(form)
        else:
            print('form invalid')
            # import pdb
            # pdb.set_trace()
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        created_by = "admin"
        created_ip = "192.168.2.48"
        project_parent = form.data['parent']
        project_code = form.data['subproject_code']
        project_name = form.data['subproject_name']
        project_id = self.model.objects.filter(parent_id=project_parent).count()
        project_id += 1
        obj = form.save(commit=False)
        obj.project_id = form.cleaned_data['project_id'] = project_id
        obj.project_code = form.cleaned_data['project_code'] = project_code
        obj.project_name = form.cleaned_data['project_name'] = project_name
        obj.created_by = form.cleaned_data['created_by'] = created_by
        obj.created_ip = form.cleaned_data['created_ip'] = created_ip
        obj.modified_by = form.cleaned_data['modified_by'] = created_by
        print(project_code)
        # import pdb
        # pdb.set_trace()
        obj.save()

        return HttpResponseRedirect(self.get_success_url())


class Subprojectlistview(ListView):
    """
      Returns a list of Timesheet sub project details that is child project  details
get_children()
      """
    model = ProjectDetails
    template_name = "superadmin/sub_project_grid.html"

    def get_context_data(self, **kwargs):

        try:
            context = super(Subprojectlistview, self).get_context_data(**kwargs)
            listof_project = self.model.objects.get(id=self.kwargs['subproject_id'])

            list_of_project = listof_project.get_children()
            # import pdb
            # pdb.set_trace()

            context = {'child_project_details': list_of_project}

        except:
            # import pdb
            # pdb.set_trace()
            context = {'child_project_details': range(1)}

        return context
