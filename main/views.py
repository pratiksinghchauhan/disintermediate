# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import listedTransfers
import whois

# Create your views here.
# def transferDomain(request):
#      if request.method == "POST":
#          sellerName = request.POST['sellerName']
#          buyerName = request.POST['buyerName']
#          sellerUpi = request.POST['sellerUpi']

         
def transferDomain(request):
    if request.method == "POST":
        payeeVa = request.POST['payee-va']
        payerVa = request.POST['payer-va']
        mobileBuyer = request.POST['mobile-buyer']
        mobileSeller = request.POST['mobile-seller']
        accountno = request.POST['payee-ac']
        amount = request.POST['amount']
        return render(request,"index.html",{"msg":"Your mandate is created, Leave rest on us, payment will automatically be done when the domain is transfered"})
    return render(request,"index.html",{"msg":""})