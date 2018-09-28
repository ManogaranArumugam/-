from django.http import request
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView


class Department_view(TemplateView):
    template_name = "superadmin/department_grid.html"

    def get_context_data(self, **kwargs):
        context = { 'range' : range(100)}
        return context


class Department_form(TemplateView):
    template_name = "superadmin/department_form.html"

