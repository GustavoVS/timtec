# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import Textarea
from django.db import models
from activities.admin import ModelAdmin
from .models import *


class LessonInline(admin.TabularInline):
    model = Lesson
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 3, 'class': 'span11'})},
    }


class UnitInline(admin.TabularInline):
    model = Unit
    fields = ('title', 'video', 'activity', 'position',)


class LessonAdmin(ModelAdmin):
    list_display = ('name', 'course',)
    search_fields = ('course__name',)
    inlines = (UnitInline,)


class UnitAdmin(ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'position', 'lesson', 'video', 'activity',)


class CourseAdmin(ModelAdmin):
    list_display = ('name', 'status', 'publication',)
    inlines = (LessonInline,)


class CourseProfessorAdmin(ModelAdmin):
    list_display = ('user', 'course',)


class VideoAdmin(ModelAdmin):
    list_display = ('name', 'youtube_id',)


admin.site.register(Video, VideoAdmin)
admin.site.register(CourseProfessor, CourseProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(StudentProgress)
admin.site.register(CourseStudent)
admin.site.register(ProfessorMessage)
