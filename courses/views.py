from django.http import HttpResponse


def course_list(request):
    return HttpResponse("""
        <h1>Available Courses</h1>
        <ul>
            <li>Web Technology</li>
            <li>Artificial Intelligence</li>
            <li>Database Systems</li>
        </ul>
    """)

