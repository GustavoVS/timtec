# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from braces import views
from core.models import Course


class AdminMixin(TemplateResponseMixin, ContextMixin,):
    def get_context_data(self, **kwargs):
        context = super(AdminMixin, self).get_context_data(**kwargs)
        context['in_admin'] = True
        return context

    def get_template_names(self):
        """
        Returns two template options, either the administration specific
        or the common template
        """
        return ['administration/' + self.template_name, self.template_name]


class AdminView(views.LoginRequiredMixin, views.GroupRequiredMixin, AdminMixin, TemplateView):
    group_required = u'professors'
    raise_exception = True


class CourseAdminView(views.LoginRequiredMixin, views.GroupRequiredMixin, AdminMixin, DetailView):
    model = Course
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'
    group_required = u'professors'
    raise_exception = True
