# Generated by Django 3.1.1 on 2020-09-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='pictures/ '),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
