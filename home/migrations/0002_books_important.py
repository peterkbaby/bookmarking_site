# Generated by Django 4.2.7 on 2024-06-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
