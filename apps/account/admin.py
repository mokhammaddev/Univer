# from django.contrib import admin
# from .models import Profile
#
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user']


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


@admin.action(description='Set to student')
def set_to_student(modeladmin, request, queryset):
    queryset.update(role=0, is_staff=False)


@admin.action(description='Set to teacher')
def set_to_teacher(modeladmin, request, queryset):
    queryset.update(role=1, is_staff=False)


@admin.action(description='Set to stuff')
def set_to_stuff(modeladmin, request, queryset):
    queryset.update(role=2, is_staff=True)


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    actions = [set_to_student, set_to_teacher, set_to_stuff]
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'role', 'password1', 'password2')}),
    )
    list_display = ('id', 'email', 'first_name', 'last_name', 'image_tag', 'role',
                    'is_staff', 'is_active', 'is_superuser', 'date_created', 'date_modified')
    ordering = None
    readonly_fields = ('date_created', 'date_modified')
    list_filter = ('date_created', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'image', 'bio')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important date', {'fields': ('date_modified', 'date_created')}),
    )
    search_fields = ('email', 'role', 'first_name', 'last_name')


admin.site.register(Account, AccountAdmin)

