# Generated by Django 3.0.6 on 2020-06-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=500)),
                ('class_monthly_fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='instituteinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=254)),
                ('institute_line', models.CharField(max_length=300)),
                ('institute_logo', models.FileField(upload_to='images/')),
                ('institute_number', models.IntegerField()),
                ('institute_web', models.CharField(max_length=200)),
                ('institute_address', models.CharField(max_length=400)),
                ('institute_country', models.CharField(choices=[('india', 'china'), ('japan', 'uk'), ('usa', 'korea'), ('england', 'Manhattan'), ('poland', 'Staten Island')], max_length=100)),
                ('institute_rar', models.CharField(default=' ', max_length=800)),
                ('admission_fee', models.CharField(default=' ', max_length=100)),
                ('registration_fee', models.CharField(default=' ', max_length=100)),
                ('Art_material', models.CharField(default=' ', max_length=300)),
                ('Transport', models.CharField(default=' ', max_length=300)),
                ('Books', models.CharField(default=' ', max_length=300)),
                ('uniform', models.CharField(default=' ', max_length=300)),
                ('fine', models.IntegerField(default=' ')),
                ('others', models.CharField(default=' ', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=500)),
                ('subject_weightage', models.IntegerField()),
                ('subclass_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='comapp.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Studentsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(default='', max_length=30)),
                ('stu_regno', models.IntegerField(default='')),
                ('stu_profile', models.FileField(blank=True, default='', null=True, upload_to='images/')),
                ('stu_admissiondate', models.DateField(default='')),
                ('stu_discount', models.IntegerField(default='')),
                ('stu_mobileno', models.IntegerField(default='')),
                ('stu_birthdate', models.DateField(blank=True, default='', null=True)),
                ('stu_orphan', models.BooleanField(blank=True, default='', null=True)),
                ('stu_gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female'), ('o', 'other')], default='', max_length=20, null=True)),
                ('stu_caste', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('stu_school', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('stu_religion', models.CharField(blank=True, choices=[('h', 'hindu'), ('m', 'muslim'), ('s', 'sikh'), ('g', 'gujrati'), ('c', 'cristian'), ('o', 'other')], default='', max_length=20, null=True)),
                ('stu_address', models.TextField(blank=True, default='', null=True)),
                ('stu_totalchildren', models.IntegerField(blank=True, default='', null=True)),
                ('stu_fathername', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_fatheroccupation', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_fatheredu', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_fatherincome', models.FloatField(blank=True, default='', null=True)),
                ('stu_fathermobile', models.IntegerField(blank=True, default='', null=True)),
                ('stu_mothername', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_motheroccupation', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_motheredu', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('stu_motherincome', models.FloatField(blank=True, default='', null=True)),
                ('stu_motehrmobile', models.IntegerField(blank=True, default='', null=True)),
                ('stu_classname', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='comapp.classes')),
            ],
        ),
    ]
