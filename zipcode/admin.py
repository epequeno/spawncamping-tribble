from django.contrib.admin import AdminSite
from django.contrib import admin
from zipcode.models import Contractor, CareerResume, ContractorSchedule, Location
from django.utils.translation import ugettext_lazy
AdminSite.site_header = "AHS Admin"
AdminSite.site_title = ugettext_lazy('AHS Site Admin')

class ContractorAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname','areacode', 'trade', 'secondaryTrades' ,'bio', 'pic')
	fields = ('firstname', 'lastname', 'areacode', 'trade', 'secondaryTrades' ,'bio', 'pic')
	prepopulated_fields = {"firstname": ("firstname",  'lastname',)}



class CareerResumeAdmin(admin.ModelAdmin):
    list_display = ('name','address','email','phone','resume')
    fields = ('name','address','email','phone','resume')
    prepopulated_fields = {"name": ("name",)}

class ContractorScheduleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('firstname', 'start_date', 'end_date', 'title', 'description',)
        }),
        ('Location', {
            'classes': ('collapse',),
            'fields': ('location',)
        }),
    )

    list_display = ('firstname','title', 'start_date', 'end_date',)
    list_filter = ['start_date']
    search_fields = ['title']
    date_hierarchy = 'start_date'

admin.site.register(Contractor, ContractorAdmin)
admin.site.register(CareerResume, CareerResumeAdmin)
admin.site.register(ContractorSchedule, ContractorScheduleAdmin)
admin.site.register(Location)
