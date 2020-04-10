from datetime import datetime
from flask import render_template, request, session
from SimpleFrontend_Flask import app
from SimpleFrontend_Flask.JSON.Data import GetData
import json

Model = GetData.Model()
ModelGroup = GetData.ModelGroup()
LatestOrder = GetData.LatestOrder()
HotestOrder = GetData.HotestOrder()
Social = GetData.Social()
PhoneNumber = GetData.PhoneNumber()
Payment = GetData.Payment()
Order = GetData.Order()
ModelName = GetData.ModelName()

app.secret_key = b'secret::;sd;__key'
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html',
                           TitlePage='HomePage',
                           Model=Model,
                           LatestOrder=LatestOrder,
                           HotestOrder=HotestOrder,
                           Social=Social,
                           PhoneNumber=PhoneNumber)

@app.route('/About')
def about():
    return render_template('about.html',
                          TitlePage='AboutPage',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber)

@app.route('/Contact')
def contact():
    return render_template('contact.html',
                          TitlePage='ContactPage',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber)

@app.route('/Payment')
def payment():
    return render_template('payment.html',
                          TitlePage='PaymentPage',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber,
                          Payment=Payment)

@app.route('/Tracking')
def tracking():
    return render_template('tracking.html',
                          TitlePage='TrackingPage',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber)

@app.route('/Tracking/User')
def usertracking():
    return render_template('usertracking.html',
                           TitlePage='UserTrackingPage',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber)

@app.route('/Tracking/User/Track', methods=['GET', 'POST'])
def usertracking_track():
    if request.method == 'POST':
        username = request.form['UserName']
        password = request.form['PassWord']
        return render_template('usertracking_track.html',
                               TitlePage='UserTrackingPage',
                                Model=Model,
                                Social=Social,
                                PhoneNumber=PhoneNumber,
                                username=username,
                                password=password)
    else:
        return render_template('page_not_found.html')

@app.route('/Tracking/OrderCode')
def ordercodetracking():
    return render_template('codetracking.html',
                           TitlePage='OrderCodeTracking',
                          Model=Model,
                          Social=Social,
                          PhoneNumber=PhoneNumber)

@app.route('/Tracking/OrderCode/Track', methods=['GET', 'POST'])
def ordercodetracking_track():
    if request.method == 'POST':
        return render_template('page_not_found.html')
    else:
        ordercode = request.args.get('OrderCode', None)
        return render_template('ordercodetracking_track.html',
                               TitlePage='OrderCodeTracking',
                                Model=Model,
                                Social=Social,
                                PhoneNumber=PhoneNumber,
                                ordercode=ordercode)



@app.route('/Order/<modeltype_code>')
def order(modeltype_code = None):
    return render_template('model_order.html',
                           TitlePage='ModelOrder',
                            Model=Model,
                            Social=Social,
                            PhoneNumber=PhoneNumber,
                            ModelGroup=ModelGroup,
                            modeltype_code=modeltype_code,
                            Order=Order,
                            ModelName=ModelName)
@app.route('/Order/<modeltype_code>/<modelname_code>')
def order_model(modeltype_code = None, modelname_code = None):
    return render_template('modelname_order.html',
                           TitlePage='OrderPage',
                            Model=Model,
                            Social=Social,
                            PhoneNumber=PhoneNumber,
                            ModelGroup=ModelGroup,
                            modeltype_code=modeltype_code,
                            modelname_code=modelname_code,
                            Order=Order,
                            ModelName=ModelName)

@app.route('/GetOrder', methods=['GET', 'POST'])
def getorder():
    if request.method == 'POST':
        session['ordername'] = request.form['OrderCode']
        return render_template('getorder.html',
                           TitlePage='GetOrderPage',
                           Model=Model,
                           Social=Social,
                           PhoneNumber=PhoneNumber,
                           ordername=session['ordername'],
                           ModelName=ModelName,
                           Order=Order)
    else:
        if 'ordername' in session:
            return render_template('getorder.html',
                           TitlePage='GetOrderPage',
                           Model=Model,
                           Social=Social,
                           PhoneNumber=PhoneNumber,
                           ordername=session['ordername'],
                           Order=Order)
        else:
            return render_template('getorder.html',
                           TitlePage='GetOrderPage',
                           Model=Model,
                           Social=Social,
                           PhoneNumber=PhoneNumber,
                           ordername=None)

@app.route('/Order/Search/', methods=['GET', 'POST'])
def ordersearch():
    if request.method == 'POST':
        return render_template('page_not_found.html')
    else:
        order_list = []
        q = request.args.get('q', None)
        for tmp in Order:
            if Order[tmp]['OrderName'].find(q) != -1:
                order_list.append(tmp)
        if len(order_list) == 0:
            return render_template('Search_not_found.html',
                                        TitlePage='SearchPage',
                                        Model=Model,
                                        Social=Social,
                                        PhoneNumber=PhoneNumber,
                                        q=q)
        else:
            return render_template('Search.html',
                                        TitlePage='SearchPage',
                                        Model=Model,
                                        Social=Social,
                                        PhoneNumber=PhoneNumber,
                                        q=q,
                                        order_list=order_list,
                                        Order=Order)

@app.errorhandler(400)
def pagenotfound(error):
    return render_template('bad_request.html'), 400

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(500)
def pagenotfound(error):
    return render_template('internal_server_error.html'), 500