# Generated by Django 2.2 on 2020-01-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOGAPP', '0003_auto_20200110_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(blank=True, max_length=20)),
                ('passw', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog_table1',
            name='author_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='blog_table1',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
