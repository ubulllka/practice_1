from .models import Students, Group
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['Student_name', 'Student_city', 'Student_age', 'Student_group_id']

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['Group_name']
