# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'zen_lunch_app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
        ))
        db.send_create_signal(u'zen_lunch_app', ['User'])

        # Adding model 'Lunch'
        db.create_table(u'zen_lunch_app_lunch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lunch_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True)),
        ))
        db.send_create_signal(u'zen_lunch_app', ['Lunch'])

        # Adding model 'UserLunch'
        db.create_table(u'zen_lunch_app_userlunch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lunch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zen_lunch_app.Lunch'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zen_lunch_app.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'zen_lunch_app', ['UserLunch'])

        # Adding unique constraint on 'UserLunch', fields ['lunch', 'user']
        db.create_unique(u'zen_lunch_app_userlunch', ['lunch_id', 'user_id'])

        # Adding model 'UserBlacklist'
        db.create_table(u'zen_lunch_app_userblacklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blacklist_user_id', to=orm['zen_lunch_app.User'])),
            ('blocked_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blocked_user_id', to=orm['zen_lunch_app.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'zen_lunch_app', ['UserBlacklist'])

        # Adding unique constraint on 'UserBlacklist', fields ['user', 'blocked_user']
        db.create_unique(u'zen_lunch_app_userblacklist', ['user_id', 'blocked_user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserBlacklist', fields ['user', 'blocked_user']
        db.delete_unique(u'zen_lunch_app_userblacklist', ['user_id', 'blocked_user_id'])

        # Removing unique constraint on 'UserLunch', fields ['lunch', 'user']
        db.delete_unique(u'zen_lunch_app_userlunch', ['lunch_id', 'user_id'])

        # Deleting model 'User'
        db.delete_table(u'zen_lunch_app_user')

        # Deleting model 'Lunch'
        db.delete_table(u'zen_lunch_app_lunch')

        # Deleting model 'UserLunch'
        db.delete_table(u'zen_lunch_app_userlunch')

        # Deleting model 'UserBlacklist'
        db.delete_table(u'zen_lunch_app_userblacklist')


    models = {
        u'zen_lunch_app.lunch': {
            'Meta': {'object_name': 'Lunch'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lunch_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'zen_lunch_app.user': {
            'Meta': {'object_name': 'User'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'zen_lunch_app.userblacklist': {
            'Meta': {'unique_together': "(('user', 'blocked_user'),)", 'object_name': 'UserBlacklist'},
            'blocked_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blocked_user_id'", 'to': u"orm['zen_lunch_app.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blacklist_user_id'", 'to': u"orm['zen_lunch_app.User']"})
        },
        u'zen_lunch_app.userlunch': {
            'Meta': {'unique_together': "(('lunch', 'user'),)", 'object_name': 'UserLunch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lunch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zen_lunch_app.Lunch']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zen_lunch_app.User']"})
        }
    }

    complete_apps = ['zen_lunch_app']