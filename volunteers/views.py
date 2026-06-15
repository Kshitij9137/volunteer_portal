from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Volunteer
from .forms import VolunteerForm
import csv
from django.http import HttpResponse


# ─── Auth ────────────────────────────────────────────────────────────────────

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created! Welcome, {user.username}.')
            return redirect('/')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# ─── Dashboard ───────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    total    = Volunteer.objects.count()
    active   = Volunteer.objects.filter(is_active=True).count()
    inactive = Volunteer.objects.filter(is_active=False).count()
    by_skill = Volunteer.objects.values('skill').annotate(
                   count=models.Count('skill')).order_by('-count')
    by_city  = Volunteer.objects.values('city').annotate(
                   count=models.Count('city')).order_by('-count')[:5]

    return render(request, 'volunteers/dashboard.html', {
        'total'   : total,
        'active'  : active,
        'inactive': inactive,
        'by_skill': by_skill,
        'by_city' : by_city,
    })


# ─── List ─────────────────────────────────────────────────────────────────────

@login_required
def volunteer_list(request):
    volunteers = Volunteer.objects.all()

    # Search
    query = request.GET.get('q', '')
    skill = request.GET.get('skill', '')
    city  = request.GET.get('city', '')

    if query:
        volunteers = volunteers.filter(name__icontains=query)
    if skill:
        volunteers = volunteers.filter(skill=skill)
    if city:
        volunteers = volunteers.filter(city__icontains=city)

    # For dropdowns
    all_skills = Volunteer.objects.values_list('skill', flat=True).distinct()
    all_cities = Volunteer.objects.values_list('city', flat=True).distinct()

    return render(request, 'volunteers/volunteer_list.html', {
        'volunteers': volunteers,
        'query'     : query,
        'skill'     : skill,
        'city'      : city,
        'all_skills': all_skills,
        'all_cities': all_cities,
    })

# ─── Add ──────────────────────────────────────────────────────────────────────

@login_required
def volunteer_add(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer added successfully!')
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/volunteer_form.html', {
        'form' : form,
        'title': 'Add Volunteer',
    })


# ─── Edit ─────────────────────────────────────────────────────────────────────

@login_required
def volunteer_edit(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer updated successfully!')
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'volunteers/volunteer_form.html', {
        'form'     : form,
        'title'    : 'Edit Volunteer',
        'volunteer': volunteer,
    })


# ─── Delete ───────────────────────────────────────────────────────────────────

@login_required
def volunteer_delete(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        messages.success(request, f'{volunteer.name} has been deleted.')
        return redirect('volunteer_list')
    return render(request, 'volunteers/volunteer_confirm_delete.html', {
        'volunteer': volunteer,
    })


# ─── Detail ───────────────────────────────────────────────────────────────────

@login_required
def volunteer_detail(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    return render(request, 'volunteers/volunteer_detail.html', {
        'volunteer': volunteer,
    })




@login_required
def export_csv(request):
    volunteers = Volunteer.objects.all()

    # Apply same filters so export matches what user sees
    query = request.GET.get('q', '')
    skill = request.GET.get('skill', '')
    city  = request.GET.get('city', '')

    if query:
        volunteers = volunteers.filter(name__icontains=query)
    if skill:
        volunteers = volunteers.filter(skill=skill)
    if city:
        volunteers = volunteers.filter(city__icontains=city)

    # Build CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="volunteers.csv"'

    writer = csv.writer(response)
    writer.writerow(['#', 'Name', 'Email', 'Phone', 'Skill', 'City', 'Joined Date', 'Status'])

    for i, v in enumerate(volunteers, start=1):
        writer.writerow([
            i,
            v.name,
            v.email,
            v.phone,
            v.skill,
            v.city,
            v.joined_date,
            'Active' if v.is_active else 'Inactive',
        ])

    return response