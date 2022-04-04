from django.shortcuts import render, redirect
from .models import ProjectUsers, Section
from .filters import UserFilter
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.db.models import Count
from django_tables2 import SingleTableView
from .table import ProjectUsersTable

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# Create your views here.
# class HomePageView(SingleTableView):

# 	model = ProjectUsers
# 	table_class = ProjectUsersTable
# 	template_name = 'kv_app/index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
# 		return context

class FilteredHomePageView(SingleTableMixin, FilterView):

	table_class = ProjectUsersTable

	model = ProjectUsers
	template_name = 'kv_app/index.html'
	table_pagination = None
	filterset_class = UserFilter
	table_pagination=False

class UserUpdateView(UpdateView):
	model = ProjectUsers
	template_name = 'kv_app/register.html'
	fields = ['full_name', 'section']


class ReportPageView(ListView):
	
	model = ProjectUsers
	template_name = 'kv_app/report.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['sectionlist'] = self.get_queryset()
		context['sec'] = Section.objects.all()
		return context


	def get_queryset(self):
		sec = Section.objects.annotate(Count('projectusers'))
		return sec.values_list('pk','name','total_count', 'projectusers__count', 'auditorya')
		


class CreateProjectUserView(CreateView):
	model = ProjectUsers
	template_name = 'kv_app/adduser.html'
	fields = '__all__'
	
	# def get_users(self):
	# 	return print(all_users)	
	


# class SearchResultListView(FilterView):
# 	model = ProjectUsers
# 	context_object_name = 'projectuser_list'
# 	template_name = 'kv_app/index.html'
# 	filterset_class = UserFilter