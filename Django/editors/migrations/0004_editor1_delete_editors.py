# Generated by Django 4.2.6 on 2023-10-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0003_delete_post_editors_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Editors',
        ),
    ]
