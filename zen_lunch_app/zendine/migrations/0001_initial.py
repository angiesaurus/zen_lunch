# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lunch_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(unique=True, max_length=60)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('team', models.CharField(max_length=100, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'user creation time')),
                ('zen_lunch_time', models.CharField(max_length=7, choices=[(b'12pm', b'12:00 PM'), (b'12:30pm', b'12:30 PM'), (b'1:00pm', b'1:00 PM')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserBlacklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('blocked_user', models.ForeignKey(related_name='blocked_user_id', to='zendine.User')),
                ('user', models.ForeignKey(related_name='blacklist_user_id', to='zendine.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('lunch', models.ForeignKey(to='zendine.Lunch')),
                ('user', models.ForeignKey(to='zendine.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userlunch',
            unique_together=set([('lunch', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='userblacklist',
            unique_together=set([('user', 'blocked_user')]),
        ),
    ]
