from django.db import models

class Group(models.Model):
    Group_id = models.BigAutoField(auto_created=True, primary_key=True)
    Group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Group_name

    def get_absolute_url(self):
        return f'/group/{self.Group_id}'


class Students(models.Model):
    Student_id = models.BigAutoField(auto_created=True, primary_key=True)
    Student_name = models.CharField(max_length=100)
    Student_city = models.CharField(max_length=100)
    Student_age = models.PositiveIntegerField()
    Student_group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_name

    def get_absolute_url(self):
        return f'/students/'






