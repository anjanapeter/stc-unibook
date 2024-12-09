from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        # Get form data
        user_role = request.POST.get("user_role")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Validate user authentication
        user = authenticate(request, username=username, password=password)
        # if user is not None:
            # Add role-based access (optional)
            # if user.groups.filter(name=user_role).exists():
            #     login(request, user)
            #     messages.success(request, f"Welcome {user_role.capitalize()}!")
                # Redirect based on role
        if user_role == "admin":
                    return redirect("admin_dashboard")
        elif user_role == "faculty":
                    return redirect("faculty_home")
        elif user_role == "student":
                    return redirect("student_dashboard")
        #     else:
        #         messages.error(request, "You do not have permission for this role.")
        # else:
        #     messages.error(request, "Invalid username or password.")
    
    return render(request, "my_app/login.html")

    
def faculty_home(request):
    return render(request, 'my_app/faculty_home.html',{})
def submit_form(request):
    return render(request, 'my_app/submit_form.html',{})
def calendar(request):
    return render(request, 'my_app/calendar.html',{})
def available_halls(request):
    return render(request, 'my_app/available_halls.html',{})
from django.shortcuts import render, redirect
from .models import Hall, Event

def submit_form(request):
    if request.method == 'POST':
        # Retrieve form data
        department_name = request.POST['department_name']
        event_name = request.POST['event_name']
        num_students = int(request.POST['num_students'])
        event_date = request.POST['event_date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        # Find available halls
        booked_halls = Event.objects.filter(
            event_date=event_date,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).values_list('hall', flat=True)

        available_halls = Hall.objects.filter(
            seats__gte=num_students
        ).exclude(id__in=booked_halls)

        # Pass data to template
        return render(request, 'my_app/available_halls.html', {
            'available_halls': available_halls,
            'department_name': department_name,
            'event_name': event_name,
            'event_date': event_date,
            'start_time': start_time,
            'end_time': end_time,
        })
    return render(request, 'my_app/submit_form.html')

def book_hall(request, hall_id):
    if request.method == 'POST':
        # Save booking
        Event.objects.create(
            department_name=request.POST['department_name'],
            event_name=request.POST['event_name'],
            num_students=request.POST['num_students'],
            event_date=request.POST['event_date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            hall_id=hall_id
        )
        return redirect('my_app/faculty_home')






