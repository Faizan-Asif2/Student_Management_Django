from django.shortcuts import render
from django.http import Http404


STUDENTS = [
    {
        'id': 1,
        'name': 'Ali Raza',
        'roll_no': 'BSCS-001',
        'cgpa': 3.65,
        'department': 'Computer Science',
        'bio': 'Interested in web development and artificial intelligence.'
    },
    {
        'id': 2,
        'name': 'Ahmed Khan',
        'roll_no': 'BSCS-002',
        'cgpa': 1.85,
        'department': 'Computer Science',
        'bio': 'Interested in databases and software engineering.'
    },
    {
        'id': 3,
        'name': 'Sara Ahmed',
        'roll_no': 'BSCS-003',
        'cgpa': 3.90,
        'department': 'Computer Science',
        'bio': 'Interested in machine learning and data science.'
    },
    {
        'id': 4,
        'name': 'Usman Ali',
        'roll_no': 'BSCS-004',
        'cgpa': 2.75,
        'department': 'Computer Science',
        'bio': 'Interested in programming and problem solving.'
    },
]


def home(request):
    return render(request, 'students/home.html', {
        'total_students': len(STUDENTS)
    })


def student_list(request):

    context = {
        'students': STUDENTS,
        'page_title': 'Student Directory',
    }

    return render(
        request,
        'students/student_list.html',
        context
    )


def student_detail(request, student_id):

    student = None

    for s in STUDENTS:
        if s['id'] == student_id:
            student = s
            break

    if student is None:
        raise Http404("Student not found")

    return render(
        request,
        'students/student_detail.html',
        {'student': student}
    )


def about(request):

    return render(request, 'students/about.html')