# Generated by Django 4.2.7 on 2024-06-15 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_books_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='bookmark',
            new_name='url',
        ),
    ]
