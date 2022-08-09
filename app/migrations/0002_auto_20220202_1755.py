# Generated by Django 3.2.5 on 2022-02-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=50)),
                ('reg_email', models.EmailField(max_length=50)),
                ('reg_phone', models.BigIntegerField()),
                ('reg_address', models.CharField(max_length=50)),
                ('reg_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='Email',
            field=models.EmailField(default='not available', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='Msg',
            field=models.CharField(default='not available', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='Name1',
            field=models.CharField(default='not available', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='Phone_no',
            field=models.BigIntegerField(default='not available'),
        ),
    ]
