from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import items
# Create your views here.

class submit(APIView):
    def post(self,request):
        if(type(request.data)!=list):
            return Response("Only list is accepted",status=status.HTTP_400_BAD_REQUEST)
        tax = {'Medicine': 0.05, 'Food': 0.05, 'Imported': 0.18, 'Book': 0, 'Music': 0.03, 'Clothes': 0.05}
        commodities={}
        totalprice=0.0
        Discount=0
        time=datetime.now()
        for i in range(len(request.data)):
            data = items(data=request.data[i])
            if data.is_valid():
                data.save()
                item = data.data['item']
                itemCategory = data.data['itemCategory']
                price = data.data['price']
                quantity = data.data['quantity']
                if itemCategory=='Clothes' and price*quantity>1000:
                    priceontax = (price * quantity) + (price * quantity * 0.12)
                else:
                    priceontax=(price * quantity) + (price * quantity * tax[itemCategory])
                totalprice+=priceontax
                commodities[item] = priceontax
            else:
                return Response("Invalid Store",status=status.HTTP_400_BAD_REQUEST)
        if totalprice > 2000:
            Discount+= (totalprice * 0.05)
            totalprice = totalprice - Discount
        response = {"DateofPurchase": time, "Item": dict(sorted(commodities.items())), "Discount": Discount,"TotalPayable": totalprice}
        return Response(response, status=status.HTTP_201_CREATED)


