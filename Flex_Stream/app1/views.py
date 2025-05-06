from django.shortcuts import render, redirect
from app1.models import UserProfile, VideoDetail, StreamingSession
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import time

# Create your views here.

def index(request):
    return render(request, 'index.html')




def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = UserProfile.objects.get(username=username)
            if check_password(password, user.password):
                # Store user info in session
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['name'] = user.name
                messages
                time.sleep(1)
                return redirect('home')
            else:
                messages.error(request, "Invalid password or username.")
        except UserProfile.DoesNotExist:
            messages.error(request, "User not found.")
    
    return render(request, 'login.html')


def is_authenticated(request):
    return request.session.get('user_id') is not None

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        # Hash the password
        hashed_password = make_password(password)

        # Create user profile
        try:
            user = UserProfile.objects.create(
                name=name,
                username=username,
                password=hashed_password,
                email=email,
                phone=phone,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT'),
            )
            user.save()
            messages.success(request, "Signup successful! Redirecting to login.")
            time.sleep(2)
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return render(request, 'signup.html')




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')





def feedback(request):
    return render(request, 'feedback.html')

def profile(request):
    return render(request,'index.html')