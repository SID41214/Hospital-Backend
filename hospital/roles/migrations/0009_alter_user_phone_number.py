# Generated by Django 5.0.3 on 2024-03-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0008_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
