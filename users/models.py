# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import random


@python_2_unicode_compatible
class User(AbstractUser):

    birthday_date = models.DateField(_("User birthday date"), blank=True, null=True)
    random_int = models.PositiveSmallIntegerField(_("Random integer"), default=random.randint(1, 100))

    def __str__(self):
        return self.username
