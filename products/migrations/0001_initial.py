# Generated by Django 4.0.3 on 2022-05-05 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.helpers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='price')),
                ('short_description', models.CharField(max_length=50, verbose_name='short description')),
                ('address', models.TextField(verbose_name='address')),
                ('apartment_type', models.CharField(choices=[('a room', 'A Room'), ('face me and face you', 'Face Me'), ('one bedroom self con', 'One Self Con'), ('two bedroom self con', 'Two Self Con'), ('three bedroom self con', 'Three Self Con'), ('duplex', 'Duplex'), ('upstairs', 'Upstairs'), ('bungalow', 'Bungalow')], max_length=30, verbose_name='apartment type')),
                ('selling_point', models.TextField(verbose_name='selling point')),
                ('home_id', models.UUIDField(default=uuid.uuid4, verbose_name='home id')),
            ],
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.helpers.get_upload_path, verbose_name='image')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='HomeAuditMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_msg', models.TextField(null=True)),
                ('album_msg', models.TextField(null=True)),
                ('short_description_msg', models.TextField(null=True)),
                ('address_msg', models.TextField(null=True)),
                ('apartment_type_msg', models.TextField(null=True)),
                ('selling_point_msg', models.TextField(null=True)),
                ('home', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.home')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.imagealbum'),
        ),
        migrations.AddField(
            model_name='home',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
