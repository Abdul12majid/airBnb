from django.contrib import admin
from .models import Profile, UserBooking
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
	model = Profile

class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ('username', 'first_name', 'last_name', 'email',)
	inlines = [ProfileInline]

admin.site.register(UserBooking)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)