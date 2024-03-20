# Generated by Django 5.0.3 on 2024-03-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('user', 'User'), ('doctor', 'Doctor'), ('admin', 'Admin')], max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
            ],
        ),
    ]