from django.core.exceptions import ImproperlyConfigured
from django.core.serializers import json
import json
from django.http import request, HttpResponseRedirect, HttpResponseForbidden, HttpResponse, QueryDict
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from tms.models import ProjectDetails
from tms.models import Department
from tms.models import Client

from tms.forms.department_form import Departmentform


class Departmentlistview(ListView):
    """
      Returns a list of Timesheet sub project details that is child project  details
get_children()
      """
    model = Department
    template_name = "superadmin/department_grid.html"

    def get_context_data(self, **kwargs):

        try:
            context = super(Departmentlistview, self).get_context_data(**kwargs)
            listof_project = self.model.objects.all()

            # list_of_project = listof_project.get_children()
            # # import pdb
            # # pdb.set_trace()

            context = {'department_details': listof_project}

        except:
            # import pdb
            # pdb.set_trace()
            context = {'department_details': range(10)}

        return context


class Departmentcreateview(CreateView):
    """Provide a way to show and handle a form in a request."""
    initial = {}
    model = Department
    form_class = Departmentform
    success_url = "superadmin/department_grid.html"
    template_name = "superadmin/department_form.html"

    # def dispatch(self, request, *args, **kwargs):
    #     # project_id = kwargs.get('project_id')
    #     # self.product = get_object_or_404(ProjectDetails, pk=project_id)
    #     return super(
    #         Departmentcreateview, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        # if not self.success_url:
        #     raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        # return str(self.success_url)  # success_url may be lazy
        return reverse_lazy('department_view')  # success_url may be lazy

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Departmentcreateview, self).get_form_kwargs(**kwargs)
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

        #
        # post_data = request.POST.copy()
        # project = ProjectDetails.objects.get(id=post_data['project'])
        # sub_project = ProjectDetails.objects.get(id=post_data['subproject'])
        # post_data['project'] = project
        # post_data['subproject'] = project
        # form = self.form_class(post_data)

        form = Departmentform(request.POST)
        project_id = request.POST.get('project')
        subproject_id = request.POST.get('subproject')
        # import pdb
        # pdb.set_trace()
        project = ProjectDetails.objects.get(id=project_id)

        try:
            subproject = ProjectDetails.objects.get(id=subproject_id)
        except:
            subproject = ProjectDetails.objects.none()

        import pdb
        pdb.set_trace()
        form.fields['project']= project
        form.fields['subproject'] = subproject
        import pdb
        pdb.set_trace()

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
        # project_parent = form.data['parent']
        # project_code = form.data['subproject_code']
        # project_name = form.data['subproject_name']
        # project_id = self.model.objects.filter(parent_id=project_parent).count()
        # project_id += 1
        import pdb
        pdb.set_trace()
        # obj = form.save(commit=False)
        # obj.project_id = form.cleaned_data['project_id'] = project_id
        # obj.project_code = form.cleaned_data['project_code'] = project_code
        # obj.project_name = form.cleaned_data['project_name'] = project_name
        # obj.created_by = form.cleaned_data['created_by'] = created_by
        # obj.created_ip = form.cleaned_data['created_ip'] = created_ip
        # obj.modified_by = form.cleaned_data['modified_by'] = created_by
        # print(project_code)
        # import pdb
        # pdb.set_trace()
        # obj.save()

        return HttpResponseRedirect(self.get_success_url())


def ProjectList_ajax(request):
    projecttype = request.GET['project_type']

    listof_project = ProjectDetails.objects.filter(parent__isnull=True, project_type=projecttype)

    projectlist = [[project.id, project.project_name, project.project_code] for project in listof_project]

    return HttpResponse(
        json.dumps(projectlist),
        content_type="application/json"
    )


def SubprojectList_ajax(request):
    project_id = request.GET['project_id']

    listofsubproject = ProjectDetails.objects.get(id=project_id)

    subproject = listofsubproject.get_children()
    projectlist = [[sproject.id, sproject.project_name, sproject.project_code] for sproject in subproject]
    # import pdb
    # pdb.set_trace()
    return HttpResponse(
        json.dumps(projectlist),
        content_type="application/json"
    )
