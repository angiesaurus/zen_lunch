# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.lunchbox_time'
        db.add_column(u'zen_lunch_app_user', 'lunchbox_time',
                      self.gf('django.db.models.fields.CharField')(default='12pm', max_length=7),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.lunchbox_time'
        db.delete_column(u'zen_lunch_app_user', 'lunchbox_time')


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
            'lunchbox_time': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
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