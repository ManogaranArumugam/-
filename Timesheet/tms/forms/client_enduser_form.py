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
from tms.models.common import Client
from tms.constants import PROJECT_STATUS, PROJECT_LIST, CLIEND_ENDUSER
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import ModelChoiceField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText


class client_enduser(BaseHorizontalForm):
    """Form for DailyTimesheet"""

    client_type = forms.ChoiceField(choices=CLIEND_ENDUSER, label="Client type", required=True)
    client_name = forms.CharField(label="Client Name", required=True)
    contact_person = forms.CharField(label="Contact person name", required=True)
    mobileno = forms.CharField(label="Mobile No.", required=True)
    telephon = forms.CharField(label="Telephone No.", required=True)
    email_id = forms.EmailField(label="Email", required=True)
    fax_no = forms.CharField(label="Fax No.", required=True)
    tin_no = forms.CharField(label="Tin No.", required=False)
    office_address = forms.CharField(
        label="Corporate Office Address",
        max_length=2000,
        required=True,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40}))
    alternate_address = forms.CharField(
        label="Project Office Address",
        max_length=2000,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40}))

    def __init__(self, *args, **kwargs):
        super(client_enduser, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Div(
                'client_type',
                'client_name',
                'contact_person',
                'mobileno',
                'telephon',
                'email_id',
                'fax_no',
                'tin_no',
                'office_address',
                'alternate_address',

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
        model = Client
        fields = (
            'client_type', 'client_name', 'contact_person', 'telephon', 'email_id', 'fax_no', 'tin_no',
            'office_address', 'alternate_address',)
