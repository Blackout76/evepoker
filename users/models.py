from django.db import models
from django.contrib.auth.models import User # to extend the basic user

class User(models.Model):
	character_name = models.TextField()
	character_id = models.IntegerField()
	user_stats =  models.OneToOneField('UserStats', on_delete=models.CASCADE)

	# Override unicode method
	def __unicode__(self):
		return self.character_name

	def getInfo(self):
		return {
			"username": self.character_name,
			"userstats": self.user_stats.getInfo()
		}


class UserStats(models.Model):
	balance = models.FloatField()
		
	def changeBalance(self, change):
		newVal = self.balance + change
		if (newVal <= 0):
			newVal = 0
		self.balance = newVal
		self.save()
		return newVal

	def getInfo(self):
		return {
			"balance": "{:,}".format(self.balance)
		}
			
