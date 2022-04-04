from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# admin.site.register(Auditorya)


class RegionResource(resources.ModelResource):
	class Meta:
		moodel = Region

class RegionAdmin(ImportExportModelAdmin):
	resourсe_class = RegionResource


class SchoolResource(resources.ModelResource):
	class Meta:
		model = School

class SchoolAdmin(ImportExportModelAdmin):
	resourсe_class = SchoolResource


class ProjectUsersResource(resources.ModelResource):
	class Meta:
		model = ProjectUsers

class ProjectUsersAdmin(ImportExportModelAdmin):
	resourсe_class = ProjectUsersResource


class SectionResource(resources.ModelResource):
	class Meta:
		model = Section

class SectionAdmin(ImportExportModelAdmin):
	resourсe_class = SectionResource

admin.site.register(Section, SectionAdmin)	
admin.site.register(ProjectUsers, ProjectUsersAdmin)

admin.site.register(Region, RegionAdmin)
admin.site.register(School, SchoolAdmin)

