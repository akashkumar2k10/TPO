from django.contrib import admin
from .models import *
# Register your models here.

class InternshipAdmin(admin.ModelAdmin):
	list_display=('id','head','body','starting_date','ending_date')

	def intern_id(self,obj):
		return obj.id

	def intern_body(self,obj):
		return obj.body
	def intern_start_date(self,obj):
		return obj.starting_date
	def intern_end_date(self,obj):
		return obj.ending_date


admin.site.register(Profile)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Jobs)
admin.site.register(AppliedIntern)


