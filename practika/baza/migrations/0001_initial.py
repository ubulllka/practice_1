# Generated by Django 4.0.4 on 2022-05-13 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('Group_id', models.AutoField(primary_key=True, serialize=False)),
                ('Group_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('Student_id', models.AutoField(primary_key=True, serialize=False)),
                ('Student_name', models.CharField(max_length=100)),
                ('Student_city', models.CharField(max_length=100)),
                ('Student_age', models.PositiveIntegerField()),
                ('Student_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.group')),
            ],
        ),
    ]
