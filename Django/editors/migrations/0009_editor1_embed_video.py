# Generated by Django 4.2.6 on 2023-10-17 14:04

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0008_alter_editor1_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor1',
            name='embed_video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
