# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
	var_x = "Come back later, this is under contruction!"
        var_y = "Don't stop believing!"
	return render(request, 'Home/home.html', {'var_x':var_x, 'var_y':var_y})
