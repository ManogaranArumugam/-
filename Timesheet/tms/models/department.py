from django.db import models
from django.db.models import PROTECT
from django.db.models import DateField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from tms.models.job import ProjectDetails
from tms.models.common import master_department
from tms.models.common import Client
from tms.models.common import Project_status
from tms.constants import PROJECT_STATUS, PROJECT_LIST, CLIEND_ENDUSER


# Create project details models.
class Department(models.Model):
    project = models.ForeignKey(ProjectDetails, related_name='project', on_delete=PROTECT)
    subproject = models.ForeignKey(ProjectDetails, related_name='subproject', on_delete=PROTECT, null=True, blank=True)
    department = models.ForeignKey(master_department, related_name='department', on_delete=PROTECT)
    dept_head = models.ForeignKey(master_department, related_name='dept_head', on_delete=PROTECT)
    dept_manager = models.ForeignKey(master_department, related_name='dept_manager', on_delete=PROTECT)
    estimation_hr = models.IntegerField(null=True, blank=True)
    databank = models.IntegerField(null=True, blank=True)
    dept_startdate = DateField(null=True, blank=True)
    dept_enddate = DateField(null=True, blank=True)
    dept_status = models.ForeignKey(Project_status, on_delete=PROTECT, null=True, blank=True)
    dept_description = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    created_ip = models.GenericIPAddressField(default='192.168.2.14')
    modified_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50)
    modified_ip = models.GenericIPAddressField(default='192.168.2.14')

    class Meta:
        db_table = "4a_department_wise"
