from src.localLib.paymentGateway import FwGateway as paymentGateway
from src.models.plans import Plans


def runPlansBilling():
    """
     Process all payments requests for all clients of all plans
    """
    pg = paymentGateway() # Instanciating the paymentGateway
    plans = Plans()

    activePlans = plans.getPlans()

    for activePlanId in activePlans.keys():
        activePlanData = activePlans[activePlanId]
        subscribers = plans.getSubscribers(activePlanId)
        for subscriberId in subscribers.keys():
            subscriberData = subscribers[subscriberId]

            nextUrl=""
            try:

                nextUrl = pg.processPlanPayment(
                    subscriberData['mail'],
                    subscriberData['currency'],
                    subscriberData['amount'],
                    activePlanData['redirectUrl'],
                    subscriberData['paymentMethod'],
                    activePlanId
                )
            except Exception as e:
                print e.message
                #Logs and alerts

            print subscriberData['mail'] + ' : ' +nextUrl
            #Send the 'nextUrl' to the subscriber Mail in orther to confirm the payment


runPlansBilling()