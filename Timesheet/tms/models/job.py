from django.db import models
from django.db.models import PROTECT
from django.db.models import DateField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone

from tms.models.common import Projecttype
from tms.models.common import Client
from tms.models.common import Project_status
from tms.constants import PROJECT_STATUS, PROJECT_LIST, CLIEND_ENDUSER


class ProjectDetails(MPTTModel):
    # project_type = models.ForeignKey(Projecttype, on_delete=PROTECT, null=True, blank=True)
    project_type = models.CharField(max_length=10, choices=PROJECT_LIST,null=True, blank=True)
    project_id = models.IntegerField(blank=True)
    project_code = models.CharField(max_length=15)
    project_name = models.CharField(max_length=1000)
    # sub_project_code = models.CharField(max_length=15, null=True, blank=True)
    # sub_project_name = models.CharField(max_length=1000, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=PROTECT, db_index=True)
    client = models.ForeignKey(Client, related_name='client', on_delete=PROTECT, null=True, blank=True)
    enduser = models.ForeignKey(Client, related_name='enduser', on_delete=PROTECT, null=True, blank=True)
    # client = models.CharField(max_length=100)
    # enduser = models.CharField(max_length=100)
    project_startdate = DateField(blank=True)
    project_enddate = DateField(blank=True)
    project_year = models.CharField(max_length=10)
    project_description = models.TextField()
    project_status = models.ForeignKey(Project_status, on_delete=PROTECT, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25)
    created_ip = models.GenericIPAddressField(default='192.168.2.14')
    modified_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=25)
    modified_ip = models.GenericIPAddressField(default='192.168.2.14')

    class Meta:
        db_table = "4a_projects"
