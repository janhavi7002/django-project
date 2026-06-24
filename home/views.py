from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from datetime import date, datetime
import random


# Home Page
def index(request):
    return render(request, "index.html")


# Registration Form
def register(request):

    if request.method == "POST":

        name = request.user.username
        email = request.user.email

        admission_number = request.POST.get("admission_number")
        branch = request.POST.get("branch")
        year = request.POST.get("year")
        contact_number = request.POST.get("contact_number")
        component_name = request.POST.get("component_name")
        componentissue_date = request.POST.get("componentissue_date")
        componentdue_date = request.POST.get("componentdue_date")
        faculty_referred = request.POST.get("faculty_referred")

        # Email validation
        if not email.endswith("student.mes.ac.in"):
            return render(
                request,
                "furm.html",
                {"error": "Only MES email IDs are allowed."}
            )

        # Phone validation
        if not contact_number.isdigit() or len(contact_number) != 10:
            return render(
                request,
                "furm.html",
                {"error": "Enter a valid 10-digit phone number."}
            )

        # Year validation
        if year not in ["1", "2", "3", "4"]:
            return render(
                request,
                "furm.html",
                {"error": "Year must be between 1 and 4."}
            )

        Student.objects.create(
            name=name,
            email=email,
            admission_number=admission_number,
            branch=branch,
            year=year,
            contact_number=contact_number,
            component_name=component_name,
            componentissue_date=componentissue_date,
            componentdue_date=componentdue_date,
            faculty_referred=faculty_referred
        )

        return render(
            request,
            "furm.html",
            {"success": "Component request submitted successfully!"}
        )

    return render(request, "furm.html")


# Login Page
def login_page(request):
    return render(request, "login.html")


# Signup Page
def signup_page(request):
    return render(request, "signup.html")


# Signup Logic
def signup_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():

            return render(
                request,
                "signup.html",
                {"error": "Email already registered."}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login.html/")

    return render(request, "signup.html")


# Login Logic + OTP
def login_user(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        try:

            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:

                otp = random.randint(100000, 999999)

                request.session["otp"] = str(otp)
                request.session["user_id"] = user.id

                print("OTP =", otp)

                send_mail(
                    "Makers Studio Login OTP",
                    f"Your OTP is {otp}",
                    "yourgmail@gmail.com",
                    [user.email],
                    fail_silently=False,
                )

                return redirect("/verify-otp/")

            return render(
                request,
                "login.html",
                {"error": "Incorrect Password"}
            )

        except User.DoesNotExist:

            return render(
                request,
                "login.html",
                {"error": "No account found with this email"}
            )

    return render(request, "login.html")


def verify_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get("otp")
        stored_otp = request.session.get("otp")

        if entered_otp == stored_otp:

            user_id = request.session.get("user_id")

            if user_id:
                user = User.objects.get(id=user_id)
                login(request, user)

            request.session.pop("otp", None)
            request.session.pop("user_id", None)

            return redirect("/dashboard/")

        return render(
            request,
            "verify_otp.html",
            {"error": "Invalid OTP"}
        )

    return render(request, "verify_otp.html")

# Dashboard
def dashboard(request):
    return render(request, "dashboard.html")


# Profile
def profile(request):

    records = Student.objects.filter(
        email=request.user.email
    ).first()

    return render(
        request,
        "profile.html",
        {"student": records}
    )


# History
def history(request):

    records = Student.objects.filter(
        email=request.user.email
    ).order_by("-id")

    return render(
        request,
        "history.html",
        {"records": records}
    )


# Notifications
def notifications(request):

    records = Student.objects.filter(
        email=request.user.email
    )

    reminders = []

    today = date.today()

    for item in records:

        try:

            due_date = datetime.strptime(
                str(item.componentdue_date),
                "%Y-%m-%d"
            ).date()

            days_left = (due_date - today).days

            if 0 <= days_left <= 2:

                reminders.append(
                    f"{item.component_name} must be returned in {days_left} day(s)."
                )

            elif days_left < 0:

                reminders.append(
                    f"{item.component_name} is overdue!"
                )

        except:
            pass

    return render(
        request,
        "notifications.html",
        {"reminders": reminders}
    )