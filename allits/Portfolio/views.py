# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def start_portfolio(request):
	return render(request, 'Portfolio/portfolio.html')
