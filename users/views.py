# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import get_object_or_404
from .forms import MyUserCreationForm, MyUserChangeForm

from .models import User


class UserDetailView(DetailView):
    model = User

    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserChangeView(UpdateView):
    form_class = MyUserChangeForm
    slug_field = "username"
    slug_url_kwarg = "username"

    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.POST.get('username')})


class UserListView(ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserDeleteView(RedirectView):

    permanent = True
    url = reverse_lazy('users:list')
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        user.delete()
        return super(UserDeleteView, self).get_redirect_url(*args, **kwargs)


class UserCreateView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/create.html'