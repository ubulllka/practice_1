# Generated by Django 4.0.4 on 2022-05-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='Group_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='Student_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
