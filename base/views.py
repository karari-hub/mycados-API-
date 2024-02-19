from ast import Delete
from django.shortcuts import render, redirect
from django.http import JsonResponse
#rest framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

#rest framework for class based views 
from rest_framework.views import APIView

#rest framework token authentication permisions 
from rest_framework.permissions import IsAuthenticated

#importing q lookup method 
from django.db.models import Q

#models
from .models import Advocate, Company

#serializers 
from .serializers import AdvocateSerializer, CompanySerializer
from base import serializers


# Create your views here.





#building endpoints 
@api_view(['GET'])
def endpoints(request):
    data=['/advocates', '/advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def advocates_list(request):
    advocates = Advocate.objects.all()

    #handles GET request
    if request.method == 'GET':
        #adding serch functionality(query)
        query = request.GET.get('query')
        if query == None:
            query=''
        #filtering advocates using query 
            for advocate in advocates:
                advocate = Advocate.objects.filter(Q(username__icontains=query) & Q(bio__icontains=query))
            #serializing
                serializer = AdvocateSerializer(advocate, many=True)
                return Response(serializer.data)

    #creating new advocate using post method 
    if request.method == 'POST':
        advocate= Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio'],
            )

        serializer = AdvocateSerializer(advocate, many=True)

        return Response('')


# #class_based views
# class Advocatedetails(APIView):

#     def get_object(self, username):
#         try:
#             return Advocate.objects.get(username=username)
#         except Advocate.DoesNotExist:
#             raise 

#     def get(self, request, username):
#         advocate = self.get_object(username)
#         serializer = AdvocateSerializer(advocate, many=True)
#         return Response(serializer.data)

#     def put(self, request, username):
#         advocate = self.get_object(username)
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         serilizer = AdvocateSerializer(advocate, many=True)
#         return Response(serilizer.data)
    
#     def delete(self, request, username):
#         advocate = self.get_object(username)
#         advocate.delete()
#         return redirect('advocates')



#function based views


@api_view(['GET', 'PUT', 'DELETE'])
def advocte_details(request, username):
    #getting username from models and passing it to username here
    advocate = Advocate.objects.get(username=username)


    if request.method == 'GET':
        #serializing 
        serialilzer = AdvocateSerializer(advocate, many=True)
        return Response(serialilzer.data)
    
    #Updating a user "PUT"
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        #serializing 
        serialilzer = AdvocateSerializer(advocate, many=True)
        return Response(serialilzer.data)       
    
    #delete a user/data "DELETE"
    if request.method == 'DELETE':
        advocate.delete()
        return redirect('advocates')


#companies views 
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return Response(serializer.data)