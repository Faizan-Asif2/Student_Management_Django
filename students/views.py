from django.http import HttpResponse


def student_list(request):
    return HttpResponse("""
        <h1>Student Management System</h1>
        <p>Welcome to the Student Portal.</p>
    """)


def student_detail(request, student_id):
    return HttpResponse(f"<h1>Details of student #{student_id}</h1>")


def about(request):
    return HttpResponse(f"<p>You sent a {request.method} request to {request.path}</p>")

def about(request):
    name = request.GET.get('name')
    return HttpResponse(name)

def home(request):
    # Return "Welcome to the Student Portal"
    return HttpResponse("<p>Welcome to the Student Portal.</p>")

def course_detail(request, course_code):
    # Return "Course: CS101" for CS101
    return HttpResponse(f"<h1>Details of course #{course_code}</h1>")

def student_marks(request, student_id, marks):
    # If marks >= 50, show Pass
    # Otherwise, show Fail
    if(marks >= 50):
        return HttpResponse("<h1>Pass</h1>")
    else:
        return HttpResponse("<h1>Fail</h1>")

def welcome(request):
    return HttpResponse("<h1>Welcome to GOA Singhum</h1>")