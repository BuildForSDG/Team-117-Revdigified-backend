from .models import RDUser
from rest_framework import serializers

class RDUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RDUser
        fields = ['url','email','DOB','is_taxpayer','is_taxcollector','is_auditor','is_systemAdmin','is_staff']
        