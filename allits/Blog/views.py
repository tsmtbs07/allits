# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def start_blog(request):
	return render(request, 'Blog/blog.html')
