from django.contrib import admin
from admissions.models import Student
from admissions.models import Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Name','FatherName','ClassName','Contact']
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Name','exp','subject','contact']
# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)