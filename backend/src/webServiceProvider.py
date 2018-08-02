from flask import Flask,request,Response
from src.localLib.paymentGateway import FwGateway as PaymentGateway

app = Flask(__name__)

@app.route('/startPayment')
def startPayment():
    """
    Gives Web Service to receive and process by Demand payments
    :return: url to redirect user's browser
    """
    pg = PaymentGateway()

    nextUrl=""

    try:
        if 'mail' in request.args and 'currency' in request.args and 'amount' in request.args and 'redirectUrl' in request.args and 'paymentMethod' in request.args:

            nextUrl = pg.processByDemandPayment(
                request.args.get('mail'),
                request.args.get('currency'),
                request.args.get('amount'),
                request.args.get('redirectUrl'),
                request.args.get('paymentMethod')
            )
    except:
        pass


    resp = Response(nextUrl)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run()