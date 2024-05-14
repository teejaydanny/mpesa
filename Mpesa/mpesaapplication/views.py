from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = '0111336542'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc,callback_url)
    return HttpResponse(response)
def stk_push_callback(request):
     data = request.body
     return HttpResponse('stk-push-callback')