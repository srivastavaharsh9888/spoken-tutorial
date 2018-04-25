from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^$',views.home,name='home'),
 	url(r'^ajax/$',views.tutorial,name='tutorial'),
 	url(r'^ajax/payment_detail/$',views.payment_table,name='payment_table')
]















