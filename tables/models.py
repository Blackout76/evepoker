from django.db import models
from django import forms

# Table Model
class Table(models.Model):
	public = models.BooleanField(default=True)
	password = models.CharField(max_length=16, default="")
	name = models.CharField(max_length=32)
	currentUsers = models.IntegerField()
	tableLimit = models.FloatField()
	tableBlind = models.FloatField()
	
	def __unicode__(self):
		return self.tableType
	
	# set number of users
	def changeUsers(self, change):
		newVal = currentUsers + change
		
		# don' change max size
		if (newVal > 10 or newVal < 1):
			return -1
		else:
			self.currentUsers = newVal
			self.save()
		return newVal
		
	# close table functions
	def closeTable(self):
		self.currentUsers = 0
		return

# Form for creating new talbles
class NewTableForm(forms.Form):
	public = forms.BooleanField()
	#password = forms.CharField(max_length=16)
	tableLimit = forms.FloatField()
	tableBlind = forms.FloatField()
	name = forms.CharField(max_length=32)
