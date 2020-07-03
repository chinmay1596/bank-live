from django.shortcuts import render
from .models import Bank
from .serializers import BankSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status



class BankViewset(viewsets.ModelViewSet):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	lookup_field = 'ifsc'

	def retrieve(self, request, *args, **kwargs):
		params = kwargs
		banks = Bank.objects.filter(ifsc=params['ifsc'])
		serializer = BankSerializer(banks, many=True)
		return Response(serializer.data)

class BankListViewset(viewsets.ModelViewSet):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer
	lookup_field = 'bankname_city'

	def retrieve(self, request, *args, **kwargs):
		params = kwargs
		params_list = params['bankname_city'].split('_')
		banks = Bank.objects.filter(bank_name=params_list[0], city=params_list[1])
		serializer = BankSerializer(banks, many=True)
		return Response(serializer.data)

