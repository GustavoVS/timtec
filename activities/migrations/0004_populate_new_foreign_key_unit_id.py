# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration


class Migration(DataMigration):
    depends_on = (
        ('core', '0011_auto__add_field_unit_side_notes'),
    )

    def forwards(self, orm):
        Unit = orm['core.Unit']

        for unit in Unit.objects.all():
            if unit.activity:
                unit.activity.unit = unit
                unit.activity.save()

        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'accounts.timtecuser': {
            'Meta': {'object_name': 'TimtecUser'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'activities.activity': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Activity'},
            'data': ('jsonfield.fields.JSONField', [], {}),
            'expected': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'activities'", 'null': 'True', 'to': u"orm['core.Unit']"})
        },
        u'activities.answer': {
            'Meta': {'ordering': "['timestamp']", 'object_name': 'Answer'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Activity']"}),
            'given': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.course': {
            'Meta': {'object_name': 'Course'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Video']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'professors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'professorcourse_set'", 'symmetrical': 'False', 'through': u"orm['core.CourseProfessor']", 'to': u"orm['accounts.TimtecUser']"}),
            'pronatec': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publication': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'requirement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '64'}),
            'structure': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'studentcourse_set'", 'symmetrical': 'False', 'through': u"orm['core.CourseStudent']", 'to': u"orm['accounts.TimtecUser']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'workload': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.courseprofessor': {
            'Meta': {'unique_together': "(('user', 'course'),)", 'object_name': 'CourseProfessor'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'instructor'", 'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'core.coursestudent': {
            'Meta': {'unique_together': "(('user', 'course'),)", 'object_name': 'CourseStudent'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.TimtecUser']"})
        },
        u'core.lesson': {
            'Meta': {'ordering': "['position']", 'object_name': 'Lesson'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Course']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'draft'", 'max_length': '64'})
        },
        u'core.unit': {
            'Meta': {'ordering': "['lesson', 'position']", 'object_name': 'Unit'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'units'", 'null': 'True', 'to': u"orm['activities.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'units'", 'to': u"orm['core.Lesson']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'side_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Video']", 'null': 'True', 'blank': 'True'})
        },
        u'core.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['activities']
    symmetrical = True
