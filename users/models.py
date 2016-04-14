# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from .utils import get_random_value

import datetime


@python_2_unicode_compatible
class User(AbstractUser):

    birthday_date = models.DateField(_("User birthday date"), null=True)
    random_int = models.PositiveSmallIntegerField(_("Random integer"), default=get_random_value)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

    @cached_property
    def age(self):
        if self.birthday_date:
            return int((datetime.datetime.now().date()-self.birthday_date).days/365)
        else:
            return None
