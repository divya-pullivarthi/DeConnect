from django.contrib import admin
from signup.models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'title')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
