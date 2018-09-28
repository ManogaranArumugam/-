"""Core Constants Module"""

"""List of project types"""
PROJECT_LIST = (
    ('', "--Select a Type --"),
    ('Project', "Project"),
    ('Tender', "Tender"),
    ('R_D', "R & D")
)
"""List of project status"""
PROJECT_STATUS = (
    ('', "Select"),
    ('Active', "In-Progress"),
    ('InActive', "Closed"),
    ('Cancel', "Cancelled"),
    ('Hold', "Hold"),
    ('As-build', "As Build"),
)

CLIEND_ENDUSER = (
    ('client', 'Client'),
    ('end_user', 'End User'),

)

TIMESHEET_CODE = {
    'clientcode':'4AC',
    'endusercode':'4EU',

}