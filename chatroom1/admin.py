from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserProfile, ConversationThread, PostReply


admin.site.register(UserProfile)
admin.site.register(ConversationThread)
admin.site.register(PostReply)

'''
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
   # fk_name = 'user'

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
# modeled after stack overflow
admin.site.unregister(User)  # Unregister user to add new inline ProfileInline
admin.site.register(User, UserAdmin)  # Register User with this inline profile
'''