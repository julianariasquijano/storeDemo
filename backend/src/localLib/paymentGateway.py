"""Handles direct payment API integration"""
import requests
import time
import json
from datetime import datetime

from src.localLib.testData import *


class FwGateway:
    """
    Handles the total interaction with the Payment Gateway API
    """
    
    def __init__(self):

        #Fill this variables with your fw Data

        self.endPoint = 'https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/v2/hosted/pay'
        self.PBFPubKey = testPBFPubKey


    def sendPaymentRequest(self,email,currency,amount,redirectUrl,paymentMethod,paymentPlan=None):
        """
        Makes http connection with the Payment Gateway API
        :return: body text from API response in json format
        """

        flatJason = ""

        #transaction id support one million by second in theory. in practice I have used previously a fileSystem based blocking system to generate unique ids more eficient than a DataBase
        txRef=str(int(time.time()))+'-'+str(datetime.now().microsecond)
        postData = {
            'amount':amount,
            'customer_email':email,
            'currency':currency,
            'payment_method': paymentMethod,
            'redirect_url':redirectUrl,
            'txref':txRef,
            'PBFPubKey':self.PBFPubKey
        }
        if paymentPlan is not None:
            postData['paymentPlan']=str(paymentPlan)
            
        requestResult = requests.post(self.endPoint, postData)

        if  requestResult.status_code==200:
            flatJason=requestResult.text

        return flatJason


    def processByDemandPayment(self,email,currency,amount,redirectUrl,paymentMethod):
        """
        Process By Demand payments
        :return: url to redirect user's browser
        """

        nextUrl = ""

        flatJasonPaymentResult = self.sendPaymentRequest(email,currency,amount,redirectUrl,paymentMethod)

        try:
            paymentResultData = json.loads(flatJasonPaymentResult)
            if paymentResultData['status'] == 'success':
                nextUrl = paymentResultData['data']['link']

        except:
            # logging and alerting libraries
            pass

        return nextUrl


    def processPlanPayment(self,email,currency,amount,redirectUrl,paymentMethod,paymentPlan):
        """
        Process payments for the specified payment plans
        :return: url to redirect user's browser
        """

        flatJasonPaymentResult = self.sendPaymentRequest(email,currency,amount,redirectUrl,paymentMethod,paymentPlan)
        nextUrl = ''
        try:
            paymentResultData = json.loads(flatJasonPaymentResult)
            if paymentResultData['status'] == 'success':
                nextUrl = paymentResultData['data']['link']

        except:
            # logging and alerting libraries
            pass

        return nextUrl