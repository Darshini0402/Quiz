# Generated by Django 3.2.3 on 2021-10-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('quesno', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
    ]
