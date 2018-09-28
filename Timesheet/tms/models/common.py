from django.db import models
from django.db.models import PROTECT
from django.db.models.functions import datetime
from django.utils.datetime_safe import datetime

from mptt.models import MPTTModel, TreeForeignKey
from tms.constants import PROJECT_STATUS, PROJECT_LIST, CLIEND_ENDUSER


class Projecttype(models.Model):
    project_type = models.CharField(max_length=10, choices=PROJECT_LIST)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "4a_project_type"


# Create client AND End User  details models.
class Client(models.Model):
    client_id = models.IntegerField(blank=True)
    client_type = models.CharField(max_length=10, choices=CLIEND_ENDUSER)
    client_code = models.CharField(max_length=15)
    client_name = models.CharField(max_length=1000)
    # parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=PROTECT, db_index=True)
    tin_no = models.CharField(max_length=50, blank=True, null=True, )
    contact_person = models.CharField(max_length=15)
    telephon = models.CharField(max_length=15)
    mobileno = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=150)
    office_address = models.TextField()
    alternate_address = models.TextField()
    client_status = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25)
    created_ip = models.GenericIPAddressField(default='192.168.2.14')
    modified_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=25)
    modified_ip = models.GenericIPAddressField(default='192.168.2.14')

    class Meta:
        db_table = "4a_client_enduser"


class Project_status(models.Model):
    project_status = models.CharField(max_length=25, choices=PROJECT_STATUS)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "4a_project_status"


class master_department(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "4a_master_department"