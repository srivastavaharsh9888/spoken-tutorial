from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save

class user(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self):
		return str(self.name)


class foss(models.Model):
	contri=models.OneToOneField(user,on_delete=models.CASCADE)
	foss_name=models.CharField(max_length=100)

	def __str__(self):
		return str(self.foss_name)

class tutorial_detail(models.Model):
	foss_own=models.ForeignKey(foss,on_delete=models.CASCADE)
	tut_name=models.CharField(max_length=100)
	last_date=models.DateField()
	actual_submit_date=models.DateField(blank=True)

	def __str__(self):
		return str(self.tut_name)


class payment(models.Model):
	user_name=models.ForeignKey(user,on_delete=models.CASCADE)
	month=models.IntegerField()
	payment_user=models.IntegerField(default=0)	

	def __str__(self):
		return str(self.user_name)

def initialize_payment(sender,**kwargs):
	payment_detail=payment.objects.get_or_create(user_name=kwargs['instance'].foss_own.contri,month=kwargs['instance'].actual_submit_date.month)[0]
	payment_detail.payment_user=payment_detail.payment_user+1000				
	payment_detail.save()

post_save.connect(initialize_payment,sender=tutorial_detail)
