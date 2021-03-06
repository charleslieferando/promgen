# Copyright (c) 2017 LINE Corporation
# These sources are released under the terms of the MIT license: see LICENSE

import logging

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from promgen.notification import NotificationBase

logger = logging.getLogger(__name__)


class FormEmail(forms.Form):
    value = forms.CharField(
        required=True,
        label='Email Address'
    )
    alias = forms.CharField(
        required=False,
        help_text='Use to hide email from being displayed'
    )


class NotificationEmail(NotificationBase):
    '''
    Simple plaintext Email notification
    '''

    form = FormEmail

    def _send(self, address, data):
        subject = render_to_string('promgen/sender/email.subject.txt', data).strip()
        body = render_to_string('promgen/sender/email.body.txt', data).strip()
        send_mail(
            subject,
            body,
            self.config('sender'),
            [address]
        )
        return True
