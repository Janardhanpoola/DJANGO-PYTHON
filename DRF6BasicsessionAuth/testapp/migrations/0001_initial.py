# Generated by Django 3.1.1 on 2021-01-04 08:19

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
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=54)),
                ('esal', models.FloatField()),
                ('eadr', models.CharField(max_length=54)),
            ],
        ),
    ]