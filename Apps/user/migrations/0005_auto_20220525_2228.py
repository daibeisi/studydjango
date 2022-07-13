# Generated by Django 3.2 on 2022-05-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userinfo_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ('user',), 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='电话号码'),
        ),
    ]
