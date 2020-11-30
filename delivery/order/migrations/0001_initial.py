# Generated by Django 3.1.3 on 2020-11-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization', models.CharField(max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('delivered_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Prepearing'), ('3', 'Delivering'), ('4', 'Delivered')], default='1', max_length=20)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
    ]
