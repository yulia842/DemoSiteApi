# Generated by Django 4.2.4 on 2023-08-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_contactform_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jokes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke', models.TextField(max_length=600)),
            ],
        ),
    ]
