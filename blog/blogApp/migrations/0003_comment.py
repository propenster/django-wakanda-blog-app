# Generated by Django 3.1 on 2020-08-16 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_post_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=80)),
                ('comment_author_email', models.EmailField(max_length=254)),
                ('comment_body', models.TextField()),
                ('comment_pub_date', models.DateTimeField(auto_now_add=True)),
                ('comment_active', models.BooleanField(default=False)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogApp.post')),
            ],
            options={
                'ordering': ['-comment_pub_date'],
            },
        ),
    ]
