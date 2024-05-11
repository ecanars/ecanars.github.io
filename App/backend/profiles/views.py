from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('showprofile')  # Redirect to the profile display page
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'editstudent.html', {'form': form})


def update_profile(request, student_id):
    user = get_object_or_404(user, pk=student_id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Optionally, add a success message
            messages.success(request, 'Profile successfully updated.')
            return redirect('showprofile')  # Adjust the redirect as necessary
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'editstudent.html', {'form': form})


def show_student(request, student_id):
    profile = get_object_or_404(profile, pk=student_id)
    return render(request, 'showstudent.html', {'student': profile})


def edit_loginedstudent(request):
    return render(request, 'editstudent.html', {'student': request.user})

def edit_student(request, student_id):
    profile = get_object_or_404(profile, pk=student_id)
    return render(request, 'editstudent.html', {'student': profile})

def show_loginedstudent(request):
    return render(request, 'showstudent.html', {'student': request.user})