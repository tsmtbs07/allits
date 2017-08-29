# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def start_contact(request):
	return render(request, 'Contact/contact.html')
