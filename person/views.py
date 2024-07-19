from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Food
from .models import Category
from django.contrib.sites import requests
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics

from permissions import IsOwnerUser
from serializers import FoodSerializers, CategorySerializers


class CreateFood(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAuthenticated]


class RetriveUpdateFood(generics.RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class UpdateFood(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsOwnerUser]
    authentication_classes = [TokenAuthentication]


class ListFood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class DeleteFood(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = [IsAdminUser]


class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]


class RetriveUpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class UpdateCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsOwnerUser]
    authentication_classes = [TokenAuthentication]


class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminUser]




class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
