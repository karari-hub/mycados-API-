from itertools import count
from pyexpat import model
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate,Company

class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    #getting employee count using seializemethodfield
    def get_employee_count(self, obj):
        count= obj.advocate_set.count()
        return count

class AdvocateSerializer(ModelSerializer):
    #bypass advocate to show company name by passing company serializer
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = ['username', 'bio', 'company']