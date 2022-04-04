from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.

def only_int(value): 
   if value.isdigit()==False:
      raise ValidationError('ID contains characters')


class Region(models.Model):
	name = models.CharField(max_length=255, verbose_name="Регион")

	def __str__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=255, verbose_name="Школа")

	def __str__(self):
		return self.name

class Section(models.Model):
	CHOOSE_CLASSROOM = (
	('Пусто', 'Пусто'),
	('Ақпараттық орталық', 'Ақпараттық орталық'),
	('Г-301', 'Г-301'),
	('Г-306', 'Г-306'),
	('Г-204', 'Г-204'),
	('Г-205', 'Г-205'),
	('Г-202', 'Г-202'),
	('Г-207', 'Г-207'),
	('Г-208', 'Г-208'),
	('Г-211', 'Г-211'),
	('Г-212', 'Г-212'),
	('ФМ-202', 'ФМ-202'),
	('ФМ-201', 'ФМ-201'),
	('ФМ-104', 'ФМ-104'),
	('ФМ-101', 'ФМ-101'),
	('ХБ-101', 'ХБ-101'),
	('Т-101', 'Т-101'),
	('Т-102', 'Т-102'),
	('Т-103', 'Т-103'),
	('Т-104', 'Т-104'),
	('Кітапхана', 'Кітапхана'),
	)

	CHOOSE_COUNT_USERS = (
		('Пусто', 'Пусто'),	
		('21', '21'),
		('17', '17'),	
	)

	name = models.CharField(max_length=255, verbose_name='Секция')
	auditorya = models.CharField(max_length=100, verbose_name='Аудитория', choices=CHOOSE_CLASSROOM, default='Пусто', blank=True, null=True)
	total_count = models.CharField(max_length=20, verbose_name='Количество участников по секциям', choices=CHOOSE_COUNT_USERS, default='Пусто', blank=True, null=True)

	def __str__(self):
		return self.name




class ProjectUsers(models.Model):
	STATUS_SECTION = (
		('1 Секция', '1 Секция'),
		('2 Секция', '2 Секция'),
		('3 Секция', '3 Секция'),
		('4 Секция', '4 Секция'),
		('5 Секция', '5 Секция'),
		('6 Секция', '6 Секция'),
		('7 Секция', '7 Секция'),
		('8 Секция', '8 Секция'),
		('9 Секция', '9 Секция'),
		('10 Секция', '10 Секция'),
		('11 Секция', '11 Секция'),
		('12 Секция', '12 Секция'),
		('13 Секция', '13 Секция'),
		('14 Секция', '14 Секция'),
		('15 Секция', '15 Секция'),
		('16 Секция', '16 Секция'),
		('17 Секция', '17 Секция'),
		('18 Секция', '18 Секция'),
		('19 Секция', '19 Секция'),
		('20 Секция', '20 Секция')

)

	IIN = models.CharField(max_length=12, verbose_name="ИИН", blank=True, null=True)
	full_name = models.CharField(max_length=255, verbose_name="ФИО", blank=True, null=True)
	position = models.CharField(max_length=255, verbose_name="Должность", blank=True, null=True)
	school = models.CharField(max_length=255, verbose_name="Школа", blank=True, null=True)
	region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Регион")
	telephone = models.CharField(max_length=11, verbose_name="Телефон", blank=True, null=True)
	email = models.EmailField(verbose_name='Почта', blank=True, null=True)
	section_choose = models.CharField(max_length=255, verbose_name="Секция", choices=STATUS_SECTION, default=None, blank=True, null=True)
	section= models.ForeignKey(Section, on_delete=models.CASCADE, related_name='projectusers', blank=True, null=True, verbose_name="Секция")
	auditorya_1 = models.CharField(max_length=100, verbose_name='Аудитория', blank=True, null=True)
	
	
	
	
	
	
	


	def __str__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse('home')

# class Registration(models.Model):

# 	STATUS_SECTION = (
# 		('Проект Экспедиция «Туған елге тағзым»', 'Проект Экспедиция «Туған елге тағзым»'),
# 		('Проект «Школьное сообщество «Шаңырақ»', 'Проект «Школьное сообщество «Шаңырақ» '),
# 		('Проект «Ұрпақтар сабақтастығы»', 'Проект «Ұрпақтар сабақтастығы»'),
# 		('Проект «TED*NIS клуб» в формате «идея, достойная распространения»', 'Проект «TED*NIS клуб» в формате «идея, достойная распространения»'),
# 		('Проект «Даналық бейсенбі»', 'Проект «Даналық бейсенбі»'),
# 		('Проект «Менің өмірімде қолданылатын мақал-мәтелдер»', 'Проект «Менің өмірімде қолданылатын мақал-мәтелдер»'),
# 		('Проект «Ұлы дала ақындары» «Замандастар жырлар»', 'Проект «Ұлы дала ақындары» «Замандастар жырлар»'),
# 		('Социальная практика «10 дней на предприятии у родителей»', 'Социальная практика «10 дней на предприятии у родителей»'),
# 		('Социальная практика «Екі апта ауылда»', 'Социальная практика «Екі апта ауылда»'),
# 		('Социальная практика «Возьми ребенка на работу»', 'Социальная практика «Возьми ребенка на работу»'),
# 		('Проект «Служение обществу»', '. Проект «Служение обществу»'),
# 		('Проект «Клуб Wikipedia»', 'Проект «Клуб Wikipedia»'),
# 		('Проект «100 книг, рекомендуемых для прочтения учащимся Интеллектуальных школ»', 'Проект «100 книг, рекомендуемых для прочтения учащимся Интеллектуальных школ»'),
# 		('Проект «Қазақ әндері»', 'Проект «Қазақ әндері»'),
# 		('Проект «Жүз күйдің тарихы»', 'Проект «Жүз күйдің тарихы»'),
# 		('Проект “Bookcrossing”', 'Проект “Bookcrossing”'),
# 		('Проект “Время чтения”', 'Проект “Время чтения”'),
# 		('Проект “1.2.3”', 'Проект “1.2.3”'),
# 		('Проект “Книга покоряет мир”', 'Проект “Книга покоряет мир”'),
# 		('Проект “Memoro”','Проект “Memoro”')

# 	)

# 	IIN = models.CharField(max_length=11, verbose_name="ИИН")
# 	full_name = models.CharField(max_length=255, verbose_name="ФИО")
# 	position = models.CharField(max_length=255, verbose_name="Должность")
# 	telephone = models.CharField(max_length=200, verbose_name="Телефон")
# 	region = models.ForeignKey(Region, on_delete=models.CASCADE)
# 	school = models.ForeignKey(School, on_delete=models.CASCADE)
# 	auditorya = models.ForeignKey(Auditorya, on_delete=models.CASCADE)
# 	project = models.CharField(max_length=255, verbose_name="Секция", choices=STATUS_SECTION, default='')


# 	def __str__(self):
# 		return self.full_name


