# Generated by Django 4.2.1 on 2023-06-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wed', '0007_alter_story_grooms_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_story',
            name='fast_meet',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='main_story',
            name='he_proposed',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='main_story',
            name='love_story',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
