# Generated by Django 3.2 on 2022-04-05 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Школа')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Секция')),
                ('auditorya', models.CharField(blank=True, choices=[('Пусто', 'Пусто'), ('Ақпараттық орталық', 'Ақпараттық орталық'), ('Г-301', 'Г-301'), ('Г-306', 'Г-306'), ('Г-204', 'Г-204'), ('Г-205', 'Г-205'), ('Г-202', 'Г-202'), ('Г-207', 'Г-207'), ('Г-208', 'Г-208'), ('Г-211', 'Г-211'), ('Г-212', 'Г-212'), ('ФМ-202', 'ФМ-202'), ('ФМ-201', 'ФМ-201'), ('ФМ-104', 'ФМ-104'), ('ФМ-101', 'ФМ-101'), ('ХБ-101', 'ХБ-101'), ('Т-101', 'Т-101'), ('Т-102', 'Т-102'), ('Т-103', 'Т-103'), ('Т-104', 'Т-104'), ('Кітапхана', 'Кітапхана')], default='Пусто', max_length=100, null=True, verbose_name='Аудитория')),
                ('total_count', models.CharField(blank=True, choices=[('Пусто', 'Пусто'), ('21', '21'), ('17', '17')], default='Пусто', max_length=20, null=True, verbose_name='Количество участников по секциям')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IIN', models.TextField(blank=True, max_length=225, null=True, verbose_name='ИИН')),
                ('full_name', models.TextField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('position', models.TextField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('school', models.TextField(blank=True, max_length=255, null=True, verbose_name='Школа')),
                ('section_choose', models.TextField(blank=True, choices=[('1 Секция', '1 Секция'), ('2 Секция', '2 Секция'), ('3 Секция', '3 Секция'), ('4 Секция', '4 Секция'), ('5 Секция', '5 Секция'), ('6 Секция', '6 Секция'), ('7 Секция', '7 Секция'), ('8 Секция', '8 Секция'), ('9 Секция', '9 Секция'), ('10 Секция', '10 Секция'), ('11 Секция', '11 Секция'), ('12 Секция', '12 Секция'), ('13 Секция', '13 Секция'), ('14 Секция', '14 Секция'), ('15 Секция', '15 Секция'), ('16 Секция', '16 Секция'), ('17 Секция', '17 Секция'), ('18 Секция', '18 Секция'), ('19 Секция', '19 Секция'), ('20 Секция', '20 Секция')], default=None, max_length=255, null=True, verbose_name='Секция')),
                ('auditorya_1', models.TextField(blank=True, max_length=225, null=True, verbose_name='Аудитория')),
                ('region', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='kv_app.region', verbose_name='Регион')),
                ('section', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectusers', to='kv_app.section', verbose_name='Секция')),
            ],
        ),
    ]