from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    path('users/list', views.UserListAPIView.as_view(), name='user_list'),
    path('employees/', views.EmployeesListView.as_view(), name='employee_list'),
    path('create/employee/', views.CreateEmployeeAPIView.as_view(), name='employee_create'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/ids/', views.TaskListIDSView.as_view(), name='task_list_ids'),
    path('tasks/list/title/', views.TaskListTitleView.as_view(), name='task_list_title'),
    path('tasks/pending/', views.TaskPending.as_view(), name='task_pending'),
    path('tasks/completed/', views.TaskCompleted.as_view(), name='task_pending'),
    path('tasks/users/ids/', views.TaskUserListIDSView.as_view(), name='task_list_ids'),
    path('tasks/users/pending/', views.TaskUserPending.as_view(), name='task_list_pending'),
    path('tasks/users/completed/', views.TaskUserCompleted.as_view(), name='task_list_completed'),
    path('tasks/create', views.CreateTaskAPIView.as_view(), name='task_list_create'),
    # path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task_retrieve_update_destroy'),
]
