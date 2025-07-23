from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bug, AdminRequest, UserProfile

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class BugReportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief title of the bug'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Detailed description of the bug'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

class BugUpdateForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'status', 'priority', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show users who are admins or super admins for assignment
        admin_users = User.objects.filter(
            userprofile__role__in=['admin', 'super_admin'],
            userprofile__is_approved=True
        )
        self.fields['assigned_to'].queryset = admin_users

class AdminRequestForm(forms.ModelForm):
    class Meta:
        model = AdminRequest
        fields = ['requested_role', 'reason']
        widgets = {
            'requested_role': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Explain why you need this role'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Limit role choices based on current user role
        if user and hasattr(user, 'userprofile'):
            if user.userprofile.role == 'user':
                self.fields['requested_role'].choices = [('admin', 'Admin')]
            elif user.userprofile.role == 'admin':
                self.fields['requested_role'].choices = [('super_admin', 'Super Admin')]