#from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
 #   SliderNumericFilter
from advanced_filters.admin import AdminAdvancedFiltersMixin
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.

class InternshipAdmin(admin.ModelAdmin):
	
	list_display=('id','company_name','apply_before','Campus_date')


class JobAdmin(admin.ModelAdmin):
	list_display=('id','company_name','apply_before','Campus_date')
	
class ProfileAdmin(AdminAdvancedFiltersMixin,ImportExportActionModelAdmin,admin.ModelAdmin):
		list_display=('u_roll',
				'f_name',
				'm_name',
				'l_name',
				'full_name',
				'sem',
				'email',
				'gender',
				'PREFRENCE_first',
				'PREFRENCE_sec',
				'PREFRENCE_third',
				'Marks_10',
				'Marks_12',
				'Marks_Diploma')
		search_fields=('u_roll','f_name',)
		list_filter=('u_roll',
				'f_name',
				'm_name',
				'l_name',
				'full_name',
				'sem',
				'email',
				'gender',
				'PREFRENCE_first',
				'PREFRENCE_sec',
				'PREFRENCE_third',
				'Marks_10',
				'Marks_12',
				'Marks_Diploma')
		advanced_filter_fields=('u_roll',
				'f_name',
				'm_name',
				'l_name',
				'full_name',
				'sem',
				'email',
				'gender',
				'PREFRENCE_first',
				'PREFRENCE_sec',
				'PREFRENCE_third',
				'Marks_10',
				'Marks_12',
				'Marks_Diploma')
			

#select first_name from auth_user,student_appliedintern where student_appliedintern.user_id=auth_user.id and student_appliedintern.intern_id=20;
class AppliedInternAdmin(admin.ModelAdmin):
	list_display=('intern_id','user_id','full_name','email'
	,'u_roll','sem','gender','birth_date','contact','PREFRENCE_first',
		'PREFRENCE_sec', 
	'PREFRENCE_third',
	'Marks_10',
	'Marks_12',
	'Marks_Diploma',
	'addmission_year_BE',
	'backlog',
	'sem_1_per',
	'sem_2_per',
	'sem_3_per',
	'sem_4_per',
	'sem_5_per',
	'sem_6_per',
	'sem_7_per',
	)

	list_filter=('intern_id',)

	def id(self,obj):
		return obj.intern_id.id

	def company_head(self,obj):
		return obj.intern_id.company_name
	
	def full_name(self, obj):
		return obj.user_id.full_name
	def email(self, obj):
		return obj.user_id.email
	def u_roll(self, obj):
		return obj.user_id.u_roll
	def sem(self, obj):
		return obj.user_id.sem
	def gender(self, obj):
		return obj.user_id.gender
	def birth_date(self,obj):
		return obj.user_id.birth_date
	def contact(self,obj):
		return obj.user_id.contact
	def PREFRENCE_first(self,obj):
		return obj.user_id.PREFRENCE_first	
	def PREFRENCE_sec(self,obj):
		return obj.user_id.PREFRENCE_sec	
	def PREFRENCE_third(self,obj):
		return obj.user_id.PREFRENCE_third
	def Marks_10(self,obj):
		return obj.user_id.Marks_10	
	def Marks_12(self,obj):
		return obj.user_id.Marks_12
	def Marks_Diploma(self,obj):
		return obj.user_id.Marks_Diploma
	def backlog(self,obj):
		return obj.user_id.backlog
	def addmission_year_BE(self,obj):
		return  obj.user_id.addmission_year_BE
	def sem_1_per(self,obj):
		return obj.user_id.sem_1_per	
	def sem_2_per(self,obj):
		return obj.user_id.sem_2_per
	def sem_3_per(self,obj):
		return obj.user_id.sem_3_per
	def sem_4_per(self,obj):
		return obj.user_id.sem_4_per	
	def sem_5_per(self,obj):
		return obj.user_id.sem_5_per
	def sem_6_per(self,obj):
		return obj.user_id.sem_6_per
	def sem_7_per(self,obj):
		return obj.user_id.sem_7_per

	
	

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Jobs,JobAdmin)
admin.site.register(AppliedIntern,AppliedInternAdmin)
