# Generated by Django 3.1.1 on 2021-04-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stu_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Biology',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Chemistry',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Class',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Email_ID',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Fname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Lname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Maths',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Physics',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Section',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Stu_ID',
            field=models.IntegerField(null=True),
        ),
    ]
