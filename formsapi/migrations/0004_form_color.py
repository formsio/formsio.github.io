# Generated by Django 2.2.7 on 2019-12-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapi', '0003_auto_20191202_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
