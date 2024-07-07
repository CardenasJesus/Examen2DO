from django.urls import path
from . import views

app_name = "emp"

urlpatterns = [
    path('employee/list', views.ListEmployeesClient.as_view(), name="list_employee"),
    path('employee/create', views.EmployeeCreate.as_view(), name="create_employee"),
    path('task/list', views.ListTaskClient.as_view(), name="list_task"),
    path('task/list/ids', views.TasksIDS.as_view(), name="list_taskid"),
    path('task/list/title', views.TaskTitles.as_view(), name="list_tasktitle"),
    path('task/pending', views.TaskPending.as_view(), name="list_taskpending"),
    path('task/completed', views.TaskCompleted.as_view(), name="list_taskcompleted"),
    path('task/user/id', views.TasksUSERSIDS.as_view(), name="list_taskuserids"),
    path('task/user/pending', views.TasksUserPending.as_view(), name="list_taskuserpending"),
    path('task/user/completed', views.TaskUserCompleted.as_view(), name="list_completedUser"),
    path('task/create', views.TaskCreate.as_view(), name="task_create"),
]