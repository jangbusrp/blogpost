# Generated by Django 3.2.8 on 2021-10-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20211016_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createposts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/images'),
        ),
    ]