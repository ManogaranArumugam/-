# Generated by Django 2.0.5 on 2018-09-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0003_auto_20180919_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='master_department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': '4a_master_department',
            },
        ),
    ]
