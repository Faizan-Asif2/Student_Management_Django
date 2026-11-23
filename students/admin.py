# students/admin.py
from django.contrib import admin
from .models import Student, Department

admin.site.register(Department)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'cgpa', 'is_active','department')
    search_fields = ('name', 'roll_no')
    list_filter = ('is_active','department')
    ordering = ('roll_no',)
    list_per_page = 20
