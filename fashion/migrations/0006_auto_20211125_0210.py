# Generated by Django 3.2.9 on 2021-11-25 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0005_rename_profile_face'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceImage',
            fields=[
                ('faceId', models.AutoField(primary_key=True, serialize=False)),
                ('faceImg', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Face',
        ),
    ]
