# Generated by Django 4.2.7 on 2023-11-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myWiki', '0003_delete_ok_delete_ok2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ok2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
            ],
        ),
    ]