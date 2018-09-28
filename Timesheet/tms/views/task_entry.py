from django.http import request
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView


class Task_entry_view(TemplateView):
    template_name = "superadmin/task_entry_grid.html"

    def get_context_data(self, **kwargs):
        context = {'range': range(2000)}
        return context


class Task_entry_form(TemplateView):
    template_name = "superadmin/task_entry_form.html"


class Task_employee_enter_view(TemplateView):
    template_name = "superadmin/employee_task_entry_view.html"

    def get_context_data(self, **kwargs):
        context = {'range': range(10)}
        return context
