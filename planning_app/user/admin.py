from django.contrib import admin
import user.models as models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'email',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'id',
        'password',
        'username',
        'first_name',
        'last_name',
        'email',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.UserProfile, UserProfileAdmin)
