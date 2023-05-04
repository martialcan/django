# Generated by Django 4.2 on 2023-04-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام غذا')),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('price', models.IntegerField(default=25000, null=True, verbose_name='قیمت')),
                ('time', models.IntegerField(blank=True, default=20, verbose_name='زمان لازم')),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]