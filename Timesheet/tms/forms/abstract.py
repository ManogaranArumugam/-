"""Base class for forms"""
from django import forms
from crispy_forms.helper import FormHelper


class BaseHorizontalFormMixin(forms.Form):
    """Customized form class that better displays crispy forms"""

    def __init__(self, *args, **kwargs):
        """initializes form with desired style configuration"""
        super(BaseHorizontalFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.wrapper_class = 'item form-group'
        self.helper.label_class = 'control-label col-md-3 col-sm-3 col-xs-12'
        self.helper.field_class = 'col-md-6'
        self.helper.form_tag = False


class BaseFormMixin(forms.Form):
    """Customized form class that better displays crispy forms"""

    def __init__(self, *args, **kwargs):
        """initializes form with desired style configuration"""
        super(BaseFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form'
        self.helper.form_tag = False


class BaseHorizontalForm(forms.ModelForm, BaseHorizontalFormMixin):
    """Customized form class that better displays crispy forms"""


class BaseForm(forms.ModelForm, BaseFormMixin):
    """Customized form class that better displays crispy forms"""
