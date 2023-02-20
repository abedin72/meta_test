# Generated by Django 4.1.5 on 2023-01-31 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetaModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='Family',
            new_name='Full_Name',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='Name',
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='ProfileImage',
            field=models.ImageField(default='00-default.jpg', upload_to='ProfileImages/'),
        ),
    ]