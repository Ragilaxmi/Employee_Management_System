from django.shortcuts import render
from django.http import JsonResponse
from DBApp.models import Employee
from . serializers import EmpSerializers
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
import json

# Create your views here.

def getempapi(request):
    emp=Employee.objects.all()
    em=[{'empno':emp.empno,'empname':emp.empname} for emp in emp]
    json_obj=json.dumps(em)
    return JsonResponse(json_obj,safe=False)
@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def getemployeeapi(request):
    if request.method=='GET':
        emp=Employee.objects.all()
        paginator_obj=PageNumberPagination()
        paginator_obj.page_size=1
        page_obj=paginator_obj.paginate_queryset(emp,request)
        serializer_obj=EmpSerializers(page_obj,many=True)

        return paginator_obj.get_paginated_response(serializer_obj.data)
    if request.method=='POST':
        serializer_obj=EmpSerializers(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(serializer_obj.errors,status=HTTP_400_BAD_REQUEST)
@api_view(['PUT','GET','DELETE'])
def modifyapi(request,pk):
    def getemp(pk):
        emp=Employee.objects.get(empno=pk)
        return emp
    if request.method=='PUT':
        emp=getemp(pk)
        ser_obj=EmpSerializers(emp,data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        emp=getemp(pk)
        ser_obj=EmpSerializers(emp)
        return Response(ser_obj.data,status=HTTP_200_OK)
    if request.method=='DELETE':
        emp=getemp(pk)
        emp.delete()
        return Response(status=HTTP_200_OK)
@api_view(['GET','POST'])
def registerapi(request):
    if request.method=='POST':
        ser_obj=UserSerializer(data=request.data)
        if ser_obj.is_valid():
            uobj=ser_obj.save()
            uobj.set_password(ser_obj.validated_data['password'])
            uobj.save()
            Token.objects.create(user=uobj)
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
