# Generated by Django 4.2.7 on 2024-06-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_books_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='important_high',
            field=models.BooleanField(default=False),
        ),
    ]