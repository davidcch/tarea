import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Poll(models.Model) :
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now

	def test_was_published_recently_with_old_poll(self):
		"""
		was_published_recently() should return False for polls whose pub_date
		is older tha 1 day
		"""
		old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_poll.was_published_recently(), True)
class Choice(models.Model) :
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice