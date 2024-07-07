# forms.py
from django import forms
from django.forms.widgets import DateInput
import requests

class CreateEmployeeForm(forms.Form):
    name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Escribe el name!"}))
    last_name = forms.CharField(max_length=32, widget=forms.Textarea(attrs={"type": "text", "class": "form-control", "placeholder": "Escribe tu apellido!"}))
    email = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type": "text", "class": "form-control"}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"type": "text", "class": "form-control"}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "text", "class": "form-control"}))
    created = forms.DateField(widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    updated = forms.DateField(widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    user = forms.ChoiceField(choices=[])
    def __init__(self, *args, **kwargs):
        super(CreateEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = self.get_user_choices()

    def get_user_choices(self):
        try:
            api_url = 'http://127.0.0.1:8000/api/users/list'  # Actualiza con la URL correcta de tu API
            response = requests.get(api_url)

            if response.status_code == 200:
                users = response.json()
                choices = [(user['id'], user['username']) for user in users]
                return choices
            else:
                return []  # Devolver una lista vacía en caso de que la solicitud falle o no devuelva datos

        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud HTTP: {e}')
            return []  # Manejar la ex


class CreateTaskForm(forms.Form):
    name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Escribe el name!"}))
    description = forms.CharField(max_length=32, widget=forms.Textarea(attrs={"type": "text", "class": "form-control", "rows": 3, "placeholder": "Escribe la description!"}))
    created = forms.DateField(widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    due_date = forms.DateField(widget=DateInput(attrs={"type": "date", "class": "form-control"}))
    state = forms.ChoiceField(choices=[("PENDING", "PENDING"), ("IN_PROGRESS", "IN_PROGRESS"), ("COMPLETED", "COMPLETED")])
    employee = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.fields['employee'].choices = self.get_employee_choices()

    def get_employee_choices(self):
        try:
            api_url = 'http://localhost:8000/api/employees/'  # Actualiza con la URL correcta de tu API de empleados
            response = requests.get(api_url)

            if response.status_code == 200:
                employees = response.json()
                choices = [(employee['id'], employee['name']) for employee in employees]
                return choices
            else:
                return []  # Devolver una lista vacía en caso de que la solicitud falle o no devuelva datos

        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud HTTP: {e}')
            return [] 