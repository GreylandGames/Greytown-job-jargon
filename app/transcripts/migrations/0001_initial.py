# Generated by Django 5.0.8 on 2024-08-18 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0005_remove_transcriptmessage_transcript_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcripts', to='lessons.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcripts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'transcripts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TranscriptMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('user', 'User'), ('assistant', 'Assistant')], max_length=10)),
                ('content', models.TextField()),
                ('key_concept', models.CharField(blank=True, max_length=255, null=True)),
                ('llm_model', models.CharField(blank=True, max_length=50, null=True)),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='transcripts.transcript')),
            ],
            options={
                'db_table': 'transcript_messages',
                'ordering': ['created_at'],
            },
        ),
    ]
