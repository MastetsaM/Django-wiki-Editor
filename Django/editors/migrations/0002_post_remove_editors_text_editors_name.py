# Generated by Django 4.2.6 on 2023-10-16 22:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='editors',
            name='text',
        ),
        migrations.AddField(
            model_name='editors',
            name='name',
            field=models.CharField(default='s', max_length=50),
            preserve_default=False,
        ),
    ]
