from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

class Description(models.Model):
    description = models.TextField(1000)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True, related_name='course_id')

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, related_name='c_id')
