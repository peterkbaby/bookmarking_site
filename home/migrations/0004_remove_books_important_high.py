# Generated by Django 4.2.7 on 2024-06-14 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_books_important_high'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='important_high',
        ),
    ]