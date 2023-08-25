# Generated by Django 4.2.4 on 2023-08-24 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JobPortal', '0009_alter_company_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='company',
            name='position',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salaryfrom',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salaryterms',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salaryto',
        ),
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('salary', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=400)),
                ('experience', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('creation_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyOld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobType', models.CharField(choices=[('Full-Time', 'full-time'), ('Part-Time', 'part-time'), ('Temporary', 'temporary')], max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('salaryfrom', models.IntegerField(null=True)),
                ('salaryto', models.IntegerField(null=True)),
                ('salaryterms', models.CharField(choices=[('month', 'month'), ('week', 'week')], max_length=200, null=True)),
                ('experience', models.CharField(choices=[('Experienced', 'Experienced'), ('Intermediate', 'Intermediate'), ('Trainee', 'Trainee')], max_length=200, null=True)),
                ('Location', models.CharField(max_length=2000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=200)),
                ('resume', models.ImageField(upload_to='')),
                ('apply_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JobPortal.job')),
            ],
        ),
    ]