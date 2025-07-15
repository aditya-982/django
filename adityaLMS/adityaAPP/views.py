from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serlializers import *
from .models import *

class adityaLMSUserSignUp(APIView):
    def post(self, request):
        userdata = adityaAPPSerializer(data=request.data)
        if userdata.is_valid():
            adityaAPPUser.objects.create(**userdata.data)
            message = {"message": "User created successfully"}
            return JsonResponse(message, status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)

class adityaLMSGetUserDetails(APIView):
    def get(self, request):
        result =list(adityaAPPUser.objects.filter().values())
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK,)
    
class adityaLMSUpdateEmail(APIView):
     def put(self,request):
        userdata = adityaLMSUpdateEmailSerliazer(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            adityaAPPUser.objects.filter(number=number).update(email=email)
            message = {"message": "email updated successfully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)

class adityaLMSDeleteUser(APIView):
     def delete(self,request,number):
        adityaAPPUser.objects.filter(number=number).delete()
        message = {"message": "user deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)
