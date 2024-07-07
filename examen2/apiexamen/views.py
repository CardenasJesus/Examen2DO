from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Employee, Tasks
from .serializer import ListEmployees,ListTask,CreateEmployees,CreateTask, UserSerializer,ListTaskIDS, ListTaskTitles, ListTaskPending,ListTaskUserIDS, ListTaskUserPending
# Create your views here.
##create
class CreateEmployeeAPIView(generics.CreateAPIView):
   serializer_class = CreateEmployees

class CreateTaskAPIView(generics.CreateAPIView):
    serializer_class = CreateTask

## LIST
class EmployeesListView(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        data = ListEmployees(queryset, many=True).data
        return Response(data)

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # Define un serializer adecuado
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

## TASKS VIEWS

class TaskListView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        data = ListTask(queryset, many=True).data
        return Response(data)

class TaskListIDSView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        data = ListTaskIDS(queryset, many=True).data
        return Response(data)

class TaskListTitleView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        data = ListTaskTitles(queryset, many=True).data
        return Response(data)

class TaskPending(APIView):
    def get(self, request):
        queryset = Tasks.objects.filter(state="PENDING")
        data = ListTaskPending(queryset, many=True).data
        return Response(data)
class TaskCompleted(APIView):
    def get(self, request):
        queryset = Tasks.objects.filter(state="COMPLETED")
        data = ListTaskPending(queryset, many=True).data
        return Response(data)

class TaskUserListIDSView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        data = ListTaskUserIDS(queryset, many=True).data
        return Response(data)

class TaskUserPending(APIView):
    def get(self, request):
        queryset = Tasks.objects.filter(state="PENDING")
        data = ListTaskUserPending(queryset, many=True).data
        return Response(data)

class TaskUserCompleted(APIView):
    def get(self, request):
        queryset = Tasks.objects.filter(state="COMPLETED")
        data = ListTaskUserPending(queryset, many=True).data
        return Response(data)