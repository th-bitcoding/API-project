from django.contrib import admin
from API.models import UserApi,UserCompanyApiModel,JobProfile
# Register your models here.

@admin.register(UserApi)
class UserApiAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')

@admin.register(JobProfile)
class UserApiAdmin(admin.ModelAdmin):
    list_display = ('id','job')

@admin.register(UserCompanyApiModel)
class UserApiAdmin(admin.ModelAdmin):
    list_display = ('name','company_name','address')