# Generated by Django 3.1.3 on 2020-11-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_title',
            field=models.CharField(max_length=40),
        ),
    ]
