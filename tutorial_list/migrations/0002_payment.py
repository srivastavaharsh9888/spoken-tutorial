# Generated by Django 2.0.3 on 2018-04-05 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_user', models.IntegerField()),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tutorial_list.user')),
            ],
        ),
    ]
