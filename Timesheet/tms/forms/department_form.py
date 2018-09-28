"""Forms related to project detail """
from typing import List, Tuple

from django import forms
from django.db.models import Sum

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, MultiField
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import datetime
from django.utils.formats import get_format
from mptt import models
from django.utils.html import mark_safe

from .abstract import BaseHorizontalForm
from tms.models import Department
from tms.models import ProjectDetails
from tms.models import Projecttype
from tms.models import master_department
from tms.models import Project_status
from tms.models import Client
from tms.constants import PROJECT_STATUS, PROJECT_LIST
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField
# from tms.models import Projecttype,Client_name
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText


class Departmentform(BaseHorizontalForm):
    """Form for DailyTimesheet department wise form """

    project_type = forms.ChoiceField(choices=PROJECT_LIST, label="Project type", required=True)
    project = forms.ChoiceField(choices=[('', '-- choose a Project --')], label="Project code & Name",
                                required=True, widget=forms.Select(), )
    subproject = forms.ChoiceField(choices=[('', '-- choose a Sub Project --')], label="Sub Project Name",
                                   required=False, widget=forms.Select())

    department = forms.ModelChoiceField(
        queryset=master_department.objects.filter(code__in=['4A_CVL', '4A_ELE', '4A_TL', '4A_MEC']).order_by('name'),
        initial='1',
        label="Department Name",
        required=True, empty_label="-- Select a Department --")
    dept_head = forms.ModelChoiceField(queryset=master_department.objects.all().order_by('name'),
                                       initial='2',
                                       label="   Head Name",
                                       required=True, empty_label="-- Select a head --")
    dept_manager = forms.ModelChoiceField(queryset=master_department.objects.all().order_by('name'),
                                          initial='3',
                                          label="   Manager Name",
                                          required=True, empty_label="-- Select a manager --")

    estimation_hr = forms.DecimalField(label="Estimation (Hours)", required=True, initial=125, )
    databank = forms.DecimalField(label="Data Bank (Hours)", required=True, decimal_places=10, initial=125, )
    dept_status = forms.ModelChoiceField(queryset=Project_status.objects.all().order_by('id'),
                                         initial='1',
                                         label="Project status",
                                         required=True, empty_label="-- Select a Status --")

    dept_startdate = forms.DateField(
        label="Project startdate",

        input_formats=("%d-%m-%Y",),
        initial={'date': '28-09-2018'},
        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "fromdate",
                'format': "%d-%m-%Y",
            }))
    dept_enddate = forms.DateField(
        input_formats=("%d-%m-%Y",),
        label="Project enddate",
        initial={'date': '28-09-2018'},
        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "todate",
                'format': "%d-%m-%Y",

            }))

    dept_description = forms.CharField(
        label="Description",
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40}))

    def __init__(self, *args, **kwargs):
        super(Departmentform, self).__init__(*args, **kwargs)
        self.fields['department'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['dept_head'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['dept_manager'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['dept_status'].label_from_instance = lambda obj: "%s" % obj.project_status

        self.helper.layout = Layout(
            Div(

                'project_type',
                'project',
                'subproject',
                'department',
                'dept_head',
                'dept_manager',
                'estimation_hr',
                'databank',
                'dept_startdate',
                'dept_enddate',
                'dept_status',
                'dept_description',

                css_class='item form-group'
            ),

            # Field('project_code' ),
            # Field('taskdescription', rows="3", css_class='control-label col-md-3 col-sm-3 col-xs-12'),
            # FormActions(
            #     Submit('save', 'Submit'),
            #     Button('cancel', 'Back', css_class="btn btn-danger")
            # )

        )

    class Meta:
        """Meta Attributes"""
        model = Department
        fields = (
            'project', 'subproject', 'department', 'dept_head', 'dept_manager', 'estimation_hr', 'databank',
            'dept_startdate', 'dept_enddate', 'dept_status', 'dept_description')
