from django.shortcuts import render, redirect
from .models import Students, Group
from .forms import StudentsForm, GroupForm
from django.views.generic import DetailView, UpdateView, DeleteView


def home_page(request):
    return render(request, 'baza/home.html', {'title': 'Главаная страница'})

def get_students(request):
    s_list = Students.objects.all()
    return render(request, 'baza/students.html', {'title': 'Список студентов', 'list': s_list})

def get_group(request):
    g_list = Group.objects.all()
    return render(request, 'baza/group.html', {'title': 'Список групп', 'list': g_list})

def get_students_group(request):
    gs_list = Students.objects.all()
    return render(request, 'baza/students_group.html', {'titel': 'Cписок группы студентов', 'list':gs_list})

def add_student(request):
    error = ''
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return get_students(request)
        else:
            error = 'Форма введена неверно'
    form = StudentsForm()
    return render(request, 'baza/add_student.html', {'title': 'Добавление студента', 'name': 'Добавить студента', 'form': form, 'error' : error})

def add_group(request):
    error = ''
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return get_group(request)
        else:
            error = 'Форма введена неверно'
    form = GroupForm()
    return render(request, 'baza/add_group.html', {'title': 'Добавление группы', 'name': 'Добавить группу', 'form': form, 'error': error})


def filter(request):
    res = Students.objects.all()
    group = Group.objects.all()
    if request.method == "POST":
        data_checkbox = request.POST.getlist('checkbox')
        if len(data_checkbox) == 0:
            res = Students.objects.all()
            return render(request, "baza/filter.html", {'list': res, 'group': group, 'title': 'Фильтр'})

        if len(data_checkbox):
            k_list = Students.objects.filter(Student_group_id__in=data_checkbox)
            return render(request, "baza/filter.html", {'list': k_list, 'group': group, 'title': 'Фильтр'})

    return render(request, "baza/filter.html", {'list': res, 'group': group, 'title': 'Фильтр'})


class Group_show(DetailView):
    model = Group
    template_name = 'baza/group_inf.html'
    context_object_name = 'group'
    form_class = GroupForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Students.objects.filter(Student_group_id=self.kwargs['pk'])
        return context


class Group_update(UpdateView):
    model = Group
    template_name = 'baza/add_group.html'
    extra_context = {'title': 'Редактирование группы', 'name': 'Редактировать группу'}
    form_class = GroupForm

class Group_delete(DeleteView):
    model = Group
    context_object_name = 'group'
    template_name = 'baza/delete_group.html'
    success_url = '/group/'
    extra_context = {'title': 'Удаление группы', 'name': 'Удалить группу'}

class Student_update(UpdateView):
    model = Students
    template_name = 'baza/add_student.html'
    extra_context = {'title': 'Редактирование студента', 'name': 'Редактирование студента'}
    form_class = StudentsForm

class Student_delete(DeleteView):
    model = Students
    context_object_name = 'student'
    template_name = 'baza/delete_student.html'
    success_url = '/students/'
    extra_context = {'title': 'Удаление студента', 'name': 'Удалить студента'}
