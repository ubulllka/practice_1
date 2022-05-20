from .models import Students, Group
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['Student_name', 'Student_city', 'Student_age', 'Student_group_id']

        widgets = {
            "Student_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "Student_city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            "Student_age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
        }

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['Group_name']

        widgets = {
            "Group_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            })
        }
