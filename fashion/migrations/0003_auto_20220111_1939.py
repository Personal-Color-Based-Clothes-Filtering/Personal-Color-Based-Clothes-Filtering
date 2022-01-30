# Generated by Django 3.2.9 on 2022-01-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0002_delete_faceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('index', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('url', models.TextField(blank=True, null=True)),
                ('brand', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('discount_price', models.TextField(blank=True, null=True)),
                ('thumbnail', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('tone', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clothes',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Collar',
        ),
        migrations.DeleteModel(
            name='Hoodie',
        ),
        migrations.DeleteModel(
            name='Longsleeve',
        ),
        migrations.DeleteModel(
            name='Shirt',
        ),
        migrations.DeleteModel(
            name='Shortsleeve',
        ),
        migrations.DeleteModel(
            name='Sleeveless',
        ),
        migrations.DeleteModel(
            name='Sweat',
        ),
        migrations.DeleteModel(
            name='Sweater',
        ),
    ]
