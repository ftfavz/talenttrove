# Generated by Django 4.2.5 on 2024-05-08 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrapi', '0005_meeting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='message_time',
            new_name='posted_at',
        ),
        migrations.AddField(
            model_name='meeting',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='organizer',
            field=models.CharField(max_length=100),
        ),
    ]