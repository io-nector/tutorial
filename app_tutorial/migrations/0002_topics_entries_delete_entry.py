# Generated by Django 5.0.2 on 2024-03-03 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tutorial.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('code', models.TextField(blank=True)),
                ('links', models.TextField(blank=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tutorial.subjects')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tutorial.topics')),
            ],
        ),
        migrations.DeleteModel(
            name='entry',
        ),
    ]
