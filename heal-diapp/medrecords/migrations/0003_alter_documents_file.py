# Generated by Django 3.2.23 on 2023-12-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medrecords', '0002_alter_documents_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
