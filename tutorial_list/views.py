from __future__ import unicode_literals
from .models import user,foss,tutorial_detail,payment
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.db.models import Count	


def home(request):
	all_tutorials=tutorial_detail.objects.all()
	return render(request,"tutorial_list/home2.html",{'tutorials':all_tutorials})


def tutorial(request):
	month_number={'jan':1,'feb':2,'mar':3,
	'apr':4,'may':5,'jun':6,'jul':7,
	'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
	month=month_number[request.GET.get('month')]
	month_data=tutorial_detail.objects.values().filter(last_date__month=month)
	context={}
	if len(month_data)>=1:
		for i in range(len(month_data)):
			contri_name=tutorial_detail.objects.filter(foss_own=month_data[i]['foss_own_id'])
			month_data[i]['foss_own_id']=str(contri_name[0].foss_own.contri)
			context.update({i:month_data[i]})
	else:
		context.update({-1:"NO ONE SUBMIITED ANY TUTORIAL THIS MONTH"})
	return JsonResponse(context)


def payment_table(request):
	month_number={'jan':1,'feb':2,'mar':3,
	'apr':4,'may':5,'jun':6,'jul':7,
	'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
	month_id=month_number[request.GET.get('month')]
	month_data=payment.objects.values().filter(month=month_id)
	context={}
	if len(month_data)>=1:
		for i in range(len(month_data)):
			name_user=user.objects.get(pk=month_data[i]['user_name_id'])
			month_data[i]['user_name_id']=name_user.name
			context.update({i:month_data[i]})
	else:
		context.update({-1:"NO PAYMENTS FOR THIS MONTH"})
	return JsonResponse(context)
	