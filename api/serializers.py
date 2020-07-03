from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank
		fields = ['ifsc', 'bank_id', 'branch_name', 'address', 'city', 'district', 'state', 'bank_name']


