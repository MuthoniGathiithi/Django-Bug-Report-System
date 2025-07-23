# bugs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Bug, AdminRequest, UserProfile
from .forms import CustomUserRegistrationForm, BugReportForm, BugUpdateForm, AdminRequestForm

def home(request):
    return render(request, 'bugs/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Bug Tracker.')
            return redirect('bug_list')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'bugs/register.html', {'form': form})

@login_required
def bug_list(request):
    bugs = Bug.objects.all()
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        bugs = bugs.filter(status=status_filter)
    
    # Filter by priority
    priority_filter = request.GET.get('priority')
    if priority_filter:
        bugs = bugs.filter(priority=priority_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        bugs = bugs.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(bugs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_choices': Bug.STATUS_CHOICES,
        'priority_choices': Bug.PRIORITY_CHOICES,
        'current_filters': {
            'status': status_filter,
            'priority': priority_filter,
            'search': search_query,
        }
    }
    return render(request, 'bugs/bug_list.html', context)

@login_required
def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'bugs/bug_detail.html', {'bug': bug})

@login_required
def submit_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.submitted_by = request.user
            bug.save()
            messages.success(request, 'Bug report submitted successfully!')
            return redirect('bug_detail', pk=bug.pk)
    else:
        form = BugReportForm()
    return render(request, 'bugs/submit_bug.html', {'form': form})

@login_required
def update_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    
    # Check if user has permission to update
    user_profile = getattr(request.user, 'userprofile', None)
    if not user_profile or user_profile.role == 'user':
        messages.error(request, 'You do not have permission to update bugs.')
        return redirect('bug_detail', pk=pk)
    
    if request.method == 'POST':
        form = BugUpdateForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bug updated successfully!')
            return redirect('bug_detail', pk=pk)
    else:
        form = BugUpdateForm(instance=bug)
    
    return render(request, 'bugs/update_bug.html', {'form': form, 'bug': bug})

@login_required
def request_admin_role(request):
    # Check if user already has pending request
    existing_request = AdminRequest.objects.filter(
        user=request.user, 
        status='pending'
    ).first()
    
    if existing_request:
        messages.info(request, 'You already have a pending admin role request.')
        return redirect('profile')
    
    if request.method == 'POST':
        form = AdminRequestForm(request.POST, user=request.user)
        if form.is_valid():
            admin_request = form.save(commit=False)
            admin_request.user = request.user
            admin_request.save()
            messages.success(request, 'Admin role request submitted successfully!')
            return redirect('profile')
    else:
        form = AdminRequestForm(user=request.user)
    
    return render(request, 'bugs/request_admin.html', {'form': form})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_bugs = Bug.objects.filter(submitted_by=request.user)
    admin_requests = AdminRequest.objects.filter(user=request.user)
    
    context = {
        'user_profile': user_profile,
        'user_bugs': user_bugs,
        'admin_requests': admin_requests,
    }
    return render(request, 'bugs/profile.html', context)

@login_required
def admin_dashboard(request):
    user_profile = getattr(request.user, 'userprofile', None)
    if not user_profile or user_profile.role not in ['admin', 'super_admin']:
        messages.error(request, 'Access denied. Admin privileges required.')
        return redirect('bug_list')
    
    # Statistics
    total_bugs = Bug.objects.count()
    open_bugs = Bug.objects.filter(status='open').count()
    resolved_bugs = Bug.objects.filter(status='resolved').count()
    
    # Recent bugs
    recent_bugs = Bug.objects.all()[:5]
    
    # Admin requests (only for super admins)
    pending_requests = None
    if user_profile.role == 'super_admin':
        pending_requests = AdminRequest.objects.filter(status='pending')
    
    context = {
        'total_bugs': total_bugs,
        'open_bugs': open_bugs,
        'resolved_bugs': resolved_bugs,
        'recent_bugs': recent_bugs,
        'pending_requests': pending_requests,
        'user_role': user_profile.role,
    }
    return render(request, 'bugs/admin_dashboard.html', context)

# Create your views here.
