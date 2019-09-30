from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    institution = models.CharField(default="McMaster University", max_length= 50)
    tutorial_1_start = models.DateTimeField(blank=True, null=True)
    tutorial_1_end = models.DateTimeField(blank=True, null=True)
    tutorial_2_start = models.DateTimeField(blank=True, null = True)
    tutorial_2_end = models.DateTimeField(blank=True,null=True)
    lecture_1_start = models.DateTimeField(blank=True,null=True)
    lecture_1_end = models.DateTimeField(blank=True, null=True)
    lecture_2_start = models.DateTimeField(blank=True,null=True)
    lecture_2_end = models.DateTimeField(blank=True, null=True)
    lecture_3_start = models.DateTimeField(blank=True,null=True)
    lecture_3_end = models.DateTimeField(blank=True, null=True)
    midterm1 = models.DateTimeField(blank=True, null=True)
    midterm2 = models.DateTimeField(blank=True,null=True)
    final_exam = models.DateTimeField(blank=True,null=True)


    