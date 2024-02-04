from django.contrib import admin
from .models import User,Stock
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _




class UserAdmins(UserAdmin):
    list_display = ['id', 'email', 'is_active', ]
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {
            "fields": (
                "first_name", 
                "last_name",
                )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('id',)


admin.site.register(User, UserAdmins)

admin.site.register(Stock)