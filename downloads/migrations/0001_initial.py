# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(max_length=100, choices=[(b'source', 'Source'), (b'win32', 'Windows binary')])),
                ('location', models.CharField(max_length=250)),
                ('md5', models.CharField(max_length=250)),
                ('sha1', models.CharField(max_length=250)),
                ('size', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mirror',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.CharField(help_text=b'Python format string, following keys are available: %(location)s, %(filename)s, %(version)s, %(program)s', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program', models.CharField(max_length=100, choices=[(b'gammu', b'Gammu'), (b'wammu', b'Wammu'), (b'python-gammu', b'python-gammu')])),
                ('version', models.CharField(max_length=100)),
                ('version_int', models.IntegerField(editable=False, blank=True)),
                ('description', models.TextField()),
                ('description_html', models.TextField(editable=False, blank=True)),
                ('changelog', models.TextField(null=True, blank=True)),
                ('changelog_html', models.TextField(null=True, editable=False, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post_news', models.BooleanField(default=True)),
                ('post_tweet', models.BooleanField(default=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='download',
            name='release',
            field=models.ForeignKey(to='downloads.Release'),
            preserve_default=True,
        ),
    ]
