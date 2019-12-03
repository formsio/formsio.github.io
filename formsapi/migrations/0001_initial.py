# Generated by Django 2.2.7 on 2019-12-01 09:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile', models.ImageField(blank=True, max_length=255, null=True, upload_to='profile')),
                ('name', models.CharField(max_length=50)),
                ('domain', models.CharField(default='all', max_length=20)),
                ('link', models.CharField(blank=True, default='to call a function which returns unique link', max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_form', to='formsapi.Form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_user', to='formsapi.User')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('suggestions', models.TextField(blank=True, null=True)),
                ('hint', models.TextField(blank=True, null=True)),
                ('answer_type', models.CharField(blank=True, max_length=30, null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_form', to='formsapi.Form')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_owner', to='formsapi.User'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_form', to='formsapi.Form')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_question', to='formsapi.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_user', to='formsapi.User')),
            ],
        ),
    ]
