from django.urls import path
from tms.views import login_class
from tms.views import Project
from tms.views import client_enduser
from tms.views import department
from tms.views import team_wise
from tms.views import team_member
from tms.views import task_entry



urlpatterns = [
    path("",  login_class.home_page.as_view(), name='login_page'),
    path('logout/', login_class.logout.as_view(), name='logout'),
    path('login_landing/', login_class.Landing_page.as_view(), name='login_landing'),
    path('login_dashboard/', login_class.Dashboard.as_view(), name='login_dashboard'),
    path('client_view/', client_enduser.ClientListview.as_view(), name='client_view'),
    path('enduser_view/', client_enduser.EnduserListview.as_view(), name='enduser_view'),
    path('client_form/', client_enduser.Clientcreateview.as_view(), name='client_form'),
    path('client_form_edit/<int:client_id>', client_enduser.Clientcreateview.as_view(), name='client_form_edit'),
    path('project_view/', Project.Projectlistview.as_view(), name='project_view'),
    path('project_form/', Project.Projectcreateview.as_view(), name='project_form'),
    path('project_form_edit/<int:project_id>/', Project.Project_form.as_view(), name='project_form_edit'),
    path('sub_project_form/<int:project_id>/', Project.Subprojectcreateview.as_view(), name='sub_project_form'),
    path('sub_project_view/<int:subproject_id>/', Project.Subprojectlistview.as_view(), name='sub_project_view'),
    path('department_view/', department.Departmentlistview.as_view(), name='department_view'),
    path('department_form/', department.Departmentcreateview.as_view(), name='department_form'),
    path('project_list/', department.ProjectList_ajax, name='project_list'),
    path('sub_project_list/', department.SubprojectList_ajax, name='sub_project_list'),
    path('teamwise_form/', team_wise.Team_wise_form.as_view(), name='teamwise_form'),
    path('teamwise_grid/', team_wise.Team_wise_view.as_view(), name='teamwise_grid'),
    path('team_member_form/', team_member.Team_member_form.as_view(), name='team_member_form'),
    path('team_member_grid/', team_member.Team_member_view.as_view(), name='team_member_grid'),
    path('task_entry_form/', task_entry.Task_entry_form.as_view(), name='task_entry_form'),
    path('task_entry_grid/', task_entry.Task_entry_view.as_view(), name='task_entry_grid'),
    path('emp_task_entry_grid/', task_entry.Task_employee_enter_view.as_view(), name='emp_task_entry_grid'),
    # path('project_form/', Landing_page.Project_form, name='project_form'),
    # path('project_view/', views.Project.as_view(),name='project_view'),
    # path('login_sample/', views.Samplepage, name='samplepage'),

]
