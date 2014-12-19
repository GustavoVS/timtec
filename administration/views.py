# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from braces import views
from core.models import Course
from .forms import UserUpdateForm


User = get_user_model()


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


class AdminView(views.GroupRequiredMixin, AdminMixin, TemplateView):
    group_required = u'professors'
    raise_exception = True


class UserListView(views.SuperuserRequiredMixin, AdminMixin, ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'user_list'
    paginate_by = 50
    raise_exception = True

    def get_queryset(self):
        qs = super(UserListView, self) \
            .get_queryset() \
            .prefetch_related('groups') \
            .order_by('username')
        print self.request.GET
        if self.request.GET.get('admin', '').lower() == 'on':
            qs = qs.filter(is_superuser=True)
        if self.request.GET.get('professors', '').lower() == 'on':
            qs = qs.filter(groups__name='professors')
        if self.request.GET.get('keyword', '') != '':
            qs = qs.filter(username__icontains=self.request.GET.get('keyword'))
        return qs


class UserUpdateView(views.SuperuserRequiredMixin, AdminMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'base.html'
    raise_exception = True

    def form_valid(self, form):
        form.save()
        return self.render_to_response(self.get_context_data(form=form))

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(str(context['form'].errors))


class UserDeleteView(views.SuperuserRequiredMixin, DeleteView):
    model = User
    raise_exception = True

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse('ok')


class CourseAdminView(views.GroupRequiredMixin, AdminMixin, DetailView):
    model = Course
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'
    group_required = u'professors'
    raise_exception = True


class CourseCreateView(views.SuperuserRequiredMixin, View, ModelFormMixin):
    model = Course
    fields = ('name',)
    raise_exception = True

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        base_slug = slugify(form.instance.name)
        slug = base_slug
        i = 1
        while Course.objects.filter(slug=slug).exists():
            slug = base_slug + str(i)
            i += 1
        form.instance.slug = slug
        return super(CourseCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy('administration.courses'))

    def get_success_url(self):
        return reverse_lazy('administration.edit_course', kwargs={'course_id': self.object.id})
