# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def start_about(request):
	return render(request, 'About/about.html')
