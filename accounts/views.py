from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.db.models import Q

from accounts.forms import ProfileEditForm
from accounts.serializers import TimtecUserSerializer
from braces.views import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        if hasattr(self, 'kwargs') and 'username' in self.kwargs:
            try:
                return get_object_or_404(self.model, username=self.kwargs['username'])
            except:
                return self.request.user
        else:
            return self.request.user


class TimtecUserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    lookup_field = 'id'
    filter_fields = ('groups__name',)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    serializer_class = TimtecUserSerializer
    ordering = ('first_name', 'username',)


class UserSearchView(LoginRequiredMixin, generics.ListAPIView):
    model = get_user_model()
    serializer_class = TimtecUserSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.QUERY_PARAMS.get('name', None)
        if query is not None:
            queryset = queryset.filter(Q(first_name__icontains=query) |
                                       Q(last_name__icontains=query) |
                                       Q(username__icontains=query) |
                                       Q(email__icontains=query))
        return queryset


class StudentSearchView(LoginRequiredMixin, generics.ListAPIView):
    model = get_user_model()
    serializer_class = TimtecUserSerializer
    search_fields = ('first_name', 'last_name', 'username', 'email')

    def get_queryset(self):
        queryset = self.model.objects.all()
        course = self.request.QUERY_PARAMS.get('course', None)

        classes = self.request.user.professor_classes.all()

        if classes:
            queryset = queryset.filter(classes__in=classes)
        else:
            # FIXME: if every student is in a class, this is useless.
            if course is not None:
                queryset = queryset.filter(studentcourse_set=course)
        query = self.request.QUERY_PARAMS.get('name', None)
        if query is not None:
            queryset = queryset.filter(Q(first_name__icontains=query) |
                                       Q(last_name__icontains=query) |
                                       Q(username__icontains=query) |
                                       Q(email__icontains=query))
        return queryset
