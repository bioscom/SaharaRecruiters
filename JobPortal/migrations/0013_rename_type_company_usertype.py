# Generated by Django 4.2.4 on 2023-08-24 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortal', '0012_remove_company_jobtype_company_gender_company_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='type',
            new_name='usertype',
        ),
    ]
