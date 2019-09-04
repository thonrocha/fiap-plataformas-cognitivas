#import flask dependencies
from flask import Flask, request, make_response, jsonify

#initialize flask app
app = Flask(__name__)

#create default route
@app.route('/')
def index():
    return 'Hello World!'

def results():
    if request.method == 'POST':
        req = results.get_json(force=True)
        action = req.get('queryResult').get('action')
        return {'fulfillmentText' : 'This is a response from webhook.'}
    else:
        return {'fulfillmentText' : 'This is a response from webhook.'}

#create route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))

#run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
