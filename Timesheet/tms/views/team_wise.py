from django.http import request
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView


class Team_wise_view(TemplateView):
    template_name = "superadmin/team_wise_grid.html"

    def get_context_data(self, **kwargs):
        context = { 'range' : range(3)}
        return context


class Team_wise_form(TemplateView):
    template_name = "superadmin/team_wise_form.html"

