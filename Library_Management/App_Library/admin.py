from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import * 


class CountryMasterClass(admin.ModelAdmin):
	list_display = ('id', 'shortname', 'country_name','phonecode')
admin.site.register(CountryMaster, CountryMasterClass)

class StateMasterClass(admin.ModelAdmin):
	list_display = ('id', 'state_name', 'fk_country')
admin.site.register(StateMaster, StateMasterClass)


class CityMasterClass(admin.ModelAdmin):
	list_display = ('id', 'city_name', 'fk_state')
admin.site.register(CityMaster, CityMasterClass)




class AdminMasterClass(admin.ModelAdmin):
	list_display = ('id', 'name', 'username','password')
admin.site.register(AdminMaster, AdminMasterClass)


class EmployeeDetailsClass(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name','email', 'username', 'mobile_no')
admin.site.register(EmployeeDetails, EmployeeDetailsClass)
