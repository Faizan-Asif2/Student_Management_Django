# students/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()

    query = request.GET.get('q')
    if query:
        students = students.filter(name__icontains=query)

    context = {
        'students': students,
        'total': students.count(),
        'query': query,
    }
    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})