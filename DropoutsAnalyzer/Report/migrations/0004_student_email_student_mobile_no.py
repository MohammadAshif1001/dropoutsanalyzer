# Generated by Django 4.2.4 on 2023-09-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0003_rename_area_school_city_school_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_no',
            field=models.BigIntegerField(default=9898245213),
        ),
    ]
