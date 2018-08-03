# Generated by Django 2.0.5 on 2018-08-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=255)),
                ('member_image', models.ImageField(default='member_imageDefault', upload_to='images/')),
                ('member_info', models.TextField()),
            ],
        ),
    ]