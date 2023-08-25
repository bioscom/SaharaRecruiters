# Generated by Django 4.2.4 on 2023-08-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortal', '0005_company_jobtype_alter_candidates_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='salary',
            new_name='salaryfrom',
        ),
        migrations.AddField(
            model_name='company',
            name='salaryto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='experience',
            field=models.IntegerField(choices=[('0', 'Experienced'), ('1', 'Intermediate'), ('2', 'Trainee')], null=True),
        ),
    ]