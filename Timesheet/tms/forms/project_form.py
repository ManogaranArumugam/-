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
from tms.models import ProjectDetails
from tms.models import Projecttype
from tms.models import Project_status
from tms.models import Client
from tms.constants import PROJECT_STATUS, PROJECT_LIST
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField
# from tms.models import Projecttype,Client_name
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText


class Projecttimesheetform(BaseHorizontalForm):
    """Form for DailyTimesheet"""

    project_type = forms.ChoiceField(choices=PROJECT_LIST, label="Project type", required=True)
    client = forms.ModelChoiceField(queryset=Client.objects.filter(client_type="client").order_by('id'),
                                    label="Client Name", required=True,
                                    empty_label="-- Select a Client --")
    enduser = forms.ModelChoiceField(queryset=Client.objects.filter(client_type='end_user').order_by('id'),
                                     label="End User Name", required=True,
                                     empty_label="-- Select a End User --")
    project_status = forms.ModelChoiceField(queryset=Project_status.objects.all().order_by('id'),
                                            label="Project status",
                                            required=True, empty_label="-- Select a Status --")

    project_name = forms.CharField(label="Project Name", required=True, max_length=1000, strip=True)

    project_startdate = forms.DateField(
        label="Project startdate",

        input_formats=("%d-%m-%Y",),

        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "fromdate",
                'format': "%d-%m-%Y",
            }))
    project_enddate = forms.DateField(
        input_formats=("%d-%m-%Y",),
        label="Project enddate",
        widget=forms.DateInput(
            attrs=
            {
                'class': 'datepicker',
                'id': "todate",
                'format': "%d-%m-%Y",

            }))

    project_description = forms.CharField(
        label="Description",
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40}))

    # def clean(self):
    #     cleaned_data = super(Projecttimesheetform, self).clean()
    #     # here all fields have been validated individually,
    #     # and so cleaned_data is fully populated
    #     projectstartdate = cleaned_data.get('project_startdate')
    #     projectenddate = cleaned_data.get('project_enddate')
    #
    #     if projectstartdate:
    #         project_startdate = datetime.strptime(projectstartdate, '%d-%m-%Y')
    #         project_enddate = datetime.strptime(projectenddate, '%d-%m-%Y')
    #         if project_startdate <= project_enddate:
    #             msg = " You Wrong Date !"
    #             self.add_error('project_startdate', msg)
    #     return cleaned_data

    # def clean(self):
    #     cleaned_data = super(Projecttimesheetform, self).clean() # call the parent clean method
    #     project_startdate  = cleaned_data.get('project_startdate')
    #     # if title exists create slug from title
    #     if project_startdate:
    #         cleaned_data['project_type'] = slugify(project_startdate)
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        super(Projecttimesheetform, self).__init__(*args, **kwargs)
        self.fields['client'].label_from_instance = lambda obj: "%s" % obj.client_name
        self.fields['enduser'].label_from_instance = lambda obj: "%s" % obj.client_name
        self.fields['project_status'].label_from_instance = lambda obj: "%s" % obj.project_status
        self.helper.layout = Layout(
            Div(
                'project_type',
                'project_code',
                'project_name',
                'client',
                'enduser',
                'project_startdate',
                'project_enddate',
                'project_status',
                'project_description',

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
        model = ProjectDetails
        fields = (
            'project_type', 'project_code', 'project_name', 'project_description', 'client', 'enduser',
            'project_startdate', 'project_enddate', 'project_status')
