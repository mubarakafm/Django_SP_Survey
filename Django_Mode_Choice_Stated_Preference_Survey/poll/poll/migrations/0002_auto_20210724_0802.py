# Generated by Django 3.2.5 on 2021-07-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage_confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]
