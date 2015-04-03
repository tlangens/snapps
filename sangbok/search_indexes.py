import datetime
from haystack import indexes
from sangbok.models import *


class SongIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	#category = indexes.ForeignKey(model_attr='category')

	def get_model(self):
		return Snapsvisa
