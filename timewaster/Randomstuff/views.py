# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
import os
import csv

os.chdir('/var/www/django/timewaster/static/')

def start_randomstuff(request):
	words = []
	with open('wordfile.csv', 'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=str(u',').encode('utf-8'), quotechar=str(u'"').encode('utf-8'))
		for row in readCSV:
			words.append(row[0])
	word = random.choice(words)
	pic_url = "https://www.google.com/search?tbm=isch&q=" + word
        word = random.choice(words)
        read_url = "https://en.wikipedia.org/wiki/" + word
	word = random.choice(words)
	bing_url = "https://www.bing.com/search?q=" + word
	return render(request, 'Randomstuff/index.html', {'pic_url':pic_url, 'read_url':read_url, 'bing_url':bing_url})
