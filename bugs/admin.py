from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Bug, UserProfile, AdminRequest

# Inline UserProfile in User admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend User Admin to include profile
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# Re-register User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'submitted_by', 'assigned_to', 'created_at']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Bug Information', {
            'fields': ('title', 'description', 'priority')
        }),
        ('Status & Assignment', {
            'fields': ('status', 'assigned_to')
        }),
        ('Metadata', {
            'fields': ('submitted_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'is_approved', 'created_at']
    list_filter = ['role', 'is_approved']
    search_fields = ['user__username', 'user__email']

@admin.register(AdminRequest)
class AdminRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'requested_role', 'status', 'created_at', 'reviewed_by']
    list_filter = ['status', 'requested_role', 'created_at']
    search_fields = ['user__username', 'reason']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Request Information', {
            'fields': ('user', 'requested_role', 'reason')
        }),
        ('Review', {
            'fields': ('status', 'reviewed_by', 'reviewed_at')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
# Register your models here.
