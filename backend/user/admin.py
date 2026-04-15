from django.contrib import admin

from user.models import City, Profile, State, User

admin.site.register(State)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    list_filter = ("state",)
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "role")
    # list_filter = ("user",)
    ordering = ("email",)
    search_fields = ("email",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user", "name", "celular", "birthday", "city",)
    # list_filter = ("user",)
    ordering = ("user",)
    search_fields = ("name",)
