from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('students/', views.get_students),
    path('group/', views.get_group),
    path('students_group/', views.get_students_group),
    path('add_student/', views.add_student),
    path('add_group/', views.add_group),
    path('filter/', views.filter),
    path('group/<int:pk>/', views.Group_show.as_view(), name="group_id"),
    path('group/<int:pk>/update', views.Group_update.as_view(), name="group_update"),
    path('group/<int:pk>/delete', views.Group_delete.as_view(), name="group_delete"),
    path('students/<int:pk>/update', views.Student_update.as_view(), name="student_update"),
    path('students/<int:pk>/delete', views.Student_delete.as_view(), name="student_delete")

]