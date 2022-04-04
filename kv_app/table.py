import django_tables2 as tables
from .models import ProjectUsers, Section
import itertools
from django.forms import ChoiceField
from django_tables2.utils import A 




class ProjectUsersTable(tables.Table):
	id = tables.Column(
		attrs={
				'td':{'style':'text-align:left'
				}	
			})
	IIN = tables.Column(
		attrs={
				'td':{'style':'text-align:left'
				}	
			})
	full_name = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)
	region = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)
	position = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)
	school = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)
	section_choose = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)
	auditorya_1 = tables.Column(
			attrs={
				'td':{'style':'text-align:left'
				}	
			}
		)

	edit = tables.LinkColumn('update', text='Зарегистрировать', args=[A('pk')], \
                         orderable=False, empty_values=())

	

	class Meta:
		model = ProjectUsers
		template_name = 'django_tables2/bootstrap4.html'
		fields = ('id', 'IIN', 'full_name','region', 'position', 'school', 'section_choose', 'auditorya_1')
		

		attrs = {
            "th" : {
                "_ordering": {
                    "orderable": "orderable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`

                }
            }
        }			
        	
        