# Generated by Django 3.2.9 on 2022-01-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0010_alter_faceimage_faceimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faceimage',
            name='faceImg',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
