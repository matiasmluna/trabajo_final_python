from django.contrib import admin


from perfiles.models import User_profile

@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    class Meta:
        model = User_profile
    list_display = ['user', 'phone', 'image']