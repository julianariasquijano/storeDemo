from src.localLib.testData import *

class Plans:
    def __init__(self):
        #Make DB connections
        pass

    def getPlans(self):
        """
        Retrieve active plans from some repo
        :return: plans id list
        """
        #From DB
        return {
            434:{
                'redirectUrl':testRedirectUrl
            }
        }

    def getSubscribers(self,planId):
        """
        Retrieve subscribers asociated with a plan
        :return: subscribers registers
        """
        #Query DB for registers with the planId
        return {
            0:{
                'mail':'noexist1@no.intro',
                'currency': 'USD',
                'amount': '1',
                'paymentMethod': 'card',
            },
            1: {
                'mail': 'noexist2@no.intro',
                'currency': 'USD',
                'amount': '1',
                'paymentMethod': 'account',
            }

        }