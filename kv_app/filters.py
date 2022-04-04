import django_filters
from .models import ProjectUsers


class UserFilter(django_filters.FilterSet):

	# section = django_filters.CharField(section_name='section__name')
	class Meta:
		model = ProjectUsers
		fields = {
			'IIN': ['icontains'],
			'full_name': ['icontains'],
			'school': ['icontains'],
			
		}