# Generated by Django 2.1.5 on 2019-03-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegister', '0002_profilepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepage',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='ProfilePage',
        ),
    ]
