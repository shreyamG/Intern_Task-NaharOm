from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
import re
from authentication.models import AuthUser, Skill


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        signin_btn_txt = "Hello, {}".format(username)
        return render(request, 'home.html', {'signin_btn_txt': signin_btn_txt, 'username': username})
    else:
        signin_btn_txt = "Hello, Sign-In"        
    return render(request, 'home.html', {'signin_btn_txt': signin_btn_txt})
    # return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        gender = request.POST['gender']
        skills = request.POST.getlist('skills')
        
        
        # Server-side validation
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.")
            return redirect('/register')
        if len(username) < 4 or len(username) > 32:
            messages.error(request, 'Username must be between 4 and 32 characters.')
            return redirect('/register')
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$', pass1):
            messages.error(request, 'Password must contain at least one letter, one number, and one special character.')
            return redirect('/register')
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match.')
            return redirect('/register')
        if not gender:
            messages.error(request, 'Please select a gender.')
            return redirect('/register')
        if not skills:
            messages.error(request, 'Please select at least one skill.')
            return redirect('/register')
        
        
        
        myuser = User.objects.create_user(username = username, password = pass1)
        myuser.save()
        
        # Creating a new user with the registered user :-
        myauthuser = AuthUser.objects.create(username=username, gender=gender)

        # Add each selected skill to the user
        for skill_name in skills:
            # Get or create the skill object
            skill_obj, _ = Skill.objects.get_or_create(name=skill_name)
            myauthuser.skills.add(skill_obj)

        # Save the user object after adding skills
        myauthuser.save()
        
        # Logging-In the new user :-
        login(request, myuser)
        
        messages.success(request, "Account created successfully.")
        
        context = {}
        context.update(csrf(request))
        
        return redirect('/signin/')
        
    signin_btn_txt = "Hello, Sign-In"
    return render(request, 'register.html', {'signin_btn_txt': signin_btn_txt})


def signin(request):
    if request.user.is_authenticated:
        username = request.user.username
        signin_btn_txt = "Hello, {}".format(username)
        return render(request, 'index2.html', {'signin_btn_txt': signin_btn_txt, 'username': username})
    else:
        if request.method == "POST":
            username = request.POST['username']
            pass1 = request.POST['pass1']
            
            user = authenticate(username=username, password=pass1)
            
            context = {}
            context.update(csrf(request))
            
            if user is not None:
                login(request, user)
                # username = username
                username = user.get_username
                messages.success(request, "You're logged in successfully")
                return render(request, 'index2.html', {"username": username})
            
            else:
                messages.error(request, "Bad credentials")
                return redirect('/signin') # ('register/') IMP
        
        signin_btn_txt = "Hello, Sign-In"        
        return render(request, 'login.html', {'signin_btn_txt': signin_btn_txt})



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('/')