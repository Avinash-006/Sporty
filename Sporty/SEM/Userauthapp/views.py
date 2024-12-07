from .models import Profile


from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages, auth

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login





def projectfrontpage(request):
    return render(request, 'Userauthapp/Frontpage.html')

from SportEventapp.models import Event
from django.shortcuts import render
from SportEventapp.models import Event
from django.shortcuts import render

def calendar_page(request):
    events = Event.objects.all()  # Fetch all events for the calendar
    context = {
        'events': events,
    }
    return render(request, 'Userauthapp/CalenderPage.html', context)

def homepage(request):
    events = Event.objects.order_by('-date')[:3]  # Fetch 3 most recent events
    context = {
        'events': events,
    }
    return render(request, 'Userauthapp/HomePage.html', context)

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'Userauthapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'Userauthspp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'Userauthapp/HomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'Userauthapp/register.html')
    else:
        return render(request, 'Userauthapp/register.html')



def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('homepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('/Events/')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'Userauthapp/Login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'Userauthapp/Login.html')
    else:
        return render(request, 'Userauthapp/Login.html')

def logout(request):
    auth.logout(request)
    return redirect('homepage')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm




from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'Userauthapp/profile.html', {'form': form, 'profile': profile})


def admin(request):
    return render(request,'Userauthapp/Ahome.html')


def dashboard(request):
    return render(request,'Userauthapp/Dashboard.html')