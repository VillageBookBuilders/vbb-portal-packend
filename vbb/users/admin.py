from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    fieldsets = (
        (None, {"fields": ["password"]}),
        (_("Personal info"), {"fields": ("name", "email", "first_name", "last_name", "profileImage", "role","is_student", "is_mentor", "is_librarian")}),
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
    list_display = ["username", "email", "first_name", "last_name", "is_superuser"]
    search_fields = ["first_name", "last_name"]

    # Custom admin action
    @admin.action(description="Update missing usernames")
    def update_missing_usernames(self, request, queryset):
        for user in queryset:
            if not user.username:  # Check if username is missing
                base_username = f"{user.first_name}{user.last_name}".replace(" ", "")
                new_username = base_username
                counter = 1

                # Ensure username is unique
                while User.objects.filter(username=new_username).exists():
                    new_username = f"{base_username}{counter}"
                    counter += 1

                user.username = new_username
                user.save()

        self.message_user(request, "Usernames updated successfully.")

    # Register the custom action
    actions = ["update_missing_usernames"]

