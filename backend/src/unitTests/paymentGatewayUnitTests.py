import unittest
from src.localLib.paymentGateway import FwGateway as PaymentGateway
from src.localLib.testData import *

class testPaymentGatewayUnitTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(testPaymentGatewayUnitTest, self).__init__(*args, **kwargs)

        self.pg = PaymentGateway()

        self.testMail=testMail
        self.testPaymentMethod=testPaymentMethod
        self.testCurrency=testCurrency
        self.testAmount=testAmount
        self.testRedirectUrl=testRedirectUrl
        self.testPlan = testPlan


    def test_processByDemandPayment(self):
        self.assertIsNot(self.pg.processByDemandPayment(self.testMail,self.testCurrency,self.testAmount,self.testRedirectUrl,self.testPaymentMethod),
             '',
             'Error: Next Url is EMPTY')

    def test_processPlanPayment(self):
        self.assertIsNot(
            self.pg.processPlanPayment(self.testMail, self.testCurrency, self.testAmount, self.testRedirectUrl,self.testPaymentMethod,self.testPlan),
            '',
            'Error: Next Url is EMPTY')


if __name__ == '__main__':
    unittest.main()    