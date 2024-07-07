from django.shortcuts import render, redirect
from django.views import generic
import requests
from .forms import CreateEmployeeForm, CreateTaskForm
CreateTaskForm
class EmployeeCreate(generic.View):
    template_name = "front/create_employee.html"
    context = {}
    payload = {}
    url = "http://127.0.0.1:8000/api/create/employee/"
    response = None
    form_class = CreateEmployeeForm
    def get(self, request):
        self.context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.payload = {
                "user": request.POST.get("user"),
                "name":request.POST.get("name"),
                "last_name": request.POST.get("last_name"),
                "email": request.POST.get("email"),
                "phone": request.POST.get("phone"),
                "address": request.POST.get("address"),
                "created": request.POST.get("created"),
                "updated": request.POST.get("updated"),
        }
        self.response = requests.post(url=self.url, data=self.payload)
        return redirect("emp:list_employee")

class TaskCreate(generic.View):
    template_name = "front/create_tasks.html"
    context = {}
    payload = {}
    url = "http://127.0.0.1:8000/api/tasks/create"
    response = None
    form_class = CreateTaskForm
    def get(self, request):
        self.context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.payload = {
                "name":request.POST.get("name"),
                "description": request.POST.get("description"),
                "created": request.POST.get("created"),
                "due_date": request.POST.get("due_date"),
                "state": request.POST.get("state"),
                "employee": request.POST.get("employee"),
        }
        self.response = requests.post(url=self.url, data=self.payload)
        return redirect("emp:list_task")



# Create your views here.
class ListEmployeesClient(generic.View):
    template_name = "front/list_employee.html"
    url = "http://127.0.0.1:8000/api/employees/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "employees": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class ListTaskClient(generic.View):
    template_name = "front/list_task.html"
    url = "http://127.0.0.1:8000/api/tasks/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class TasksIDS(generic.View):
    template_name = "front/list_taskid.html"
    url = "http://127.0.0.1:8000/api/tasks/ids/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class TaskTitles(generic.View):
    template_name = "front/list_task_title.html"
    url = "http://127.0.0.1:8000/api/tasks/list/title/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class TaskPending(generic.View):
    template_name = "front/list_task_pending.html"
    url = "http://127.0.0.1:8000/api/tasks/pending/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class TaskCompleted(generic.View):
    template_name = "front/list_task_completed.html"
    url = "http://127.0.0.1:8000/api/tasks/completed/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)

class TasksUSERSIDS(generic.View):
    template_name = "front/list_task_userid.html"
    url = "http://127.0.0.1:8000/api/tasks/users/ids/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)
    
class TasksUserPending(generic.View):
    template_name = "front/list_task_user_pending.html"
    url = "http://127.0.0.1:8000/api/tasks/users/pending/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)
class TaskUserCompleted(generic.View):
    template_name = "front/list_task_user_completed.html"
    url = "http://127.0.0.1:8000/api/tasks/users/completed/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "tasks": self.response.json(),
        }
        return render(request, self.template_name, self.context)