from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.

# class InternshipAdmin(admin.ModelAdmin):
	
#     list_display=('id','head','body','starting_date','ending_date')


# class JobAdmin(admin.ModelAdmin):
# 	list_display=('id','head','body','starting_date','ending_date')

# class ProfileAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
# 	list_display=('u_roll',
#                 'f_name',
#                 'm_name',
#                 'l_name',
# 				'full_name',
#                 'sem',
#                 'email',
#                 'gender',
#                 'PREFRENCE_first',
#                 'PREFRENCE_sec',
#                 'PREFRENCE_third',
#                 'Marks_10',
#                 'Marks_12',
# 				'Marks_Diploma')
# 	search_fields=('u_roll','f_name',)
# 	list_filter=('u_roll',
#                 'f_name',
#                 'm_name',
#                 'l_name',
# 				'full_name',
#                 'sem',
#                 'email',
#                 'gender',
#                 'PREFRENCE_first',
#                 'PREFRENCE_sec',
#                 'PREFRENCE_third',
#                 'Marks_10',
#                 'Marks_12',
# 				'Marks_Diploma')

# #select first_name from auth_user,student_appliedintern where student_appliedintern.user_id=auth_user.id and student_appliedintern.intern_id=20;
# class AppliedInternAdmin(admin.ModelAdmin):
#     list_display=('intern_id','user_id')
#     search_fields=('intern_id','user_id')
# admin.site.register(Profile,ProfileAdmin)
# admin.site.register(Internship,InternshipAdmin)
# admin.site.register(Jobs,JobAdmin)
# admin.site.register(AppliedIntern,AppliedInternAdmin)

admin.site.register(Profile)
admin.site.register(Internship)
admin.site.register(Jobs)
admin.site.register(AppliedIntern)
