from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField()
