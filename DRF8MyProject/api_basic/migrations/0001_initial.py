# Generated by Django 3.1.1 on 2021-06-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
