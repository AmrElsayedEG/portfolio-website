# Generated by Django 2.2.9 on 2020-10-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('is_live', models.BooleanField(default=False)),
                ('primary_img', models.ImageField(upload_to='imgs')),
                ('secondary_img', models.ImageField(upload_to='imgs')),
                ('project_description', models.TextField()),
                ('technologies_used', models.TextField()),
                ('project_url', models.URLField(default='https://github.com/AmrElsayedEG/')),
            ],
        ),
    ]
