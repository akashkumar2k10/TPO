from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.

class InternshipAdmin(admin.ModelAdmin):
	list_display=('id','head','body','starting_date','ending_date')

class JobAdmin(admin.ModelAdmin):
	list_display=('id','head','body','starting_date','ending_date')

class ProfileAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
	list_display=('u_roll','name','sem','email','gender','PREFRENCE_first',
                'PREFRENCE_sec',
                'PREFRENCE_third',
                'Marks_10',
                'Marks_12',
				'Marks_Diploma')
	search_fields=('u_roll','name',)
	list_filter=('u_roll','name','sem','email','gender','PREFRENCE_first',
                'PREFRENCE_sec',
                'PREFRENCE_third',
                'Marks_10',
                'Marks_12',
				'Marks_Diploma')


	

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Jobs,JobAdmin)
admin.site.register(AppliedIntern)


