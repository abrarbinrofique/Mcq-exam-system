# Generated by Django 5.1.1 on 2024-09-12 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('question_type', models.CharField(choices=[('audio', 'audio'), ('text', 'text')], max_length=50)),
                ('text_option_one', models.TextField(blank=True, null=True)),
                ('text_option_two', models.TextField(blank=True, null=True)),
                ('text_option_three', models.TextField(blank=True, null=True)),
                ('text_option_four', models.TextField(blank=True, null=True)),
                ('image_option_one', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_option_two', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_option_three', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_option_four', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('ans', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.IntegerField()),
                ('get_result', models.IntegerField(blank=True, default=0, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]