# Generated by Django 2.2.5 on 2019-09-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=30)),
                ('salary', models.IntegerField(default=1000)),
                ('designation', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=3)),
            ],
        ),
    ]
