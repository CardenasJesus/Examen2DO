from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee, Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ListEmployees(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'last_name',
            'email',
            'phone',
        ]

class ListTask(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'description',
            'created',
            'due_date',
            'state',
            'employee',
        ]

class CreateEmployees(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class CreateTask(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class ListTaskIDS(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
        ]

class ListTaskTitles(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
        ]

class ListTaskPending(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'state',
        ]

class ListTaskUserIDS(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'employee',
        ]

class ListTaskUserPending(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'state',
            'employee',
        ]