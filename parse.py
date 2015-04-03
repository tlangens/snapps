from html.parser import HTMLParser
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snapps.settings")
django.setup()
from sangbok.models import *

# create a subclass and override the handler methods

class Song():
	title = ''
	predata = ''
	text = ''
	postdata = ''
	category = ''

	tempdata = ''
	tempafterb = True

	def print_song(self):
		song = Snapsvisa()
		song.name = self.title
		song.pre = self.predata
		song.lyrics = self.text
		song.post = self.postdata
		if(self.category == 'Fosterländska Sånger'):
			song.category = Category.objects.get(id=3)
		elif(self.category == 'Akademiska sånger'):
			song.category = Category.objects.get(id=4)
		elif(self.category == 'Teknologvisor'):
			song.category = Category.objects.get(id=5)
		elif(self.category == 'Snapsvisor'):
			song.category = Category.objects.get(id=6)
		elif(self.category == 'Vinvisor'):
			song.category = Category.objects.get(id=7)
		elif(self.category == 'Andra dryckesvisor'):
			song.category = Category.objects.get(id=8)
		elif(self.category == 'Punschvisor'):
			song.category = Category.objects.get(id=9)
		elif(self.category == 'Sama suomeksi'):
			song.category = Category.objects.get(id=10)
		elif(self.category == 'Diverse sånger'):
			song.category = Category.objects.get(id=11)

		song.save()
		#print('*********SONG**************')
		#print('TITLE:', self.title)
		#print('PREDATA:', self.predata)
		#print('TEXT:', self.text)
		#print('POSTDATA:', self.postdata)
		#print('CATEGORY:', self.category)
		#print('*********ENDSONG***********')

class MyHTMLParser(HTMLParser):
	song = None
	cur_tag = None

	def __init__(self, song):
		super().__init__()
		self.song = song

	def handle_starttag(self, tag, attrs):
		#print("tag:", tag)
		if(tag == 'b' and song.title != ''):
			self.song.postdata = self.song.tempdata
			self.song.tempdata = ''
			self.song.print_song()
			self.song.tempafterb = True
		self.cur_tag = tag

	def handle_endtag(self, tag):
		self.cur_tag = None

	def handle_data(self, data):
		if(self.cur_tag == 'i'):
			self.song.tempdata += data

		elif(self.cur_tag == None):
			stripdata = data.strip()
			if(stripdata != ''):
				if(self.song.tempdata != ''):
					if(self.song.tempafterb):
						self.song.predata = self.song.tempdata
						self.song.tempdata = ''
						self.song.tempafterb = False
					else:
						self.song.text += ('\n'+self.song.tempdata)
						self.song.tempdata = ''
				self.song.text += stripdata

		elif(self.cur_tag == 'b'):
			self.song.title = data
			self.song.text = ''
			self.song.predata = ''
			self.song.postdata = ''

		elif(self.cur_tag == 's'):
			self.song.category = data


song = Song()
parser = MyHTMLParser(song)
f = open('sangbok.txt')
txt = f.read()
parser.feed(txt)